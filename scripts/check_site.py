#!/usr/bin/env python3
"""Dependency-free checks against a real Jekyll production build."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote
import hashlib, json, re, sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '_site'
ORIGIN = 'https://melon-xu.github.io'
errors = []
class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.ids=[]; self.links=[]; self.canonical=[]; self.text=[]; self.articles=[]
        self.feed(path.read_text())
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='article' and 'publication' in a.get('class','').split(): self.articles.append(a.get('id'))
        if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a.get('href'))
        if tag in ('a','link') and 'href' in a:self.links.append(a['href'])
        if tag in ('img','script') and 'src' in a:self.links.append(a['src'])
        if tag=='img' and not a.get('alt'):errors.append('Image without alt text')
    def handle_data(self,data):self.text.append(data)

def route(path):
    p=OUT/unquote(path).lstrip('/')
    if p.is_dir():return p/'index.html'
    if p.exists():return p
    if not p.suffix and p.with_suffix('.html').exists():return p.with_suffix('.html')
    return p
pages={p:Page(p) for p in OUT.rglob('*.html')}
internal=0; external=set()
for path,page in pages.items():
    pageurl=ORIGIN+'/'+path.relative_to(OUT).as_posix().removesuffix('index.html')
    if len(page.ids)!=len(set(page.ids)):errors.append(f'Duplicate IDs: {path}')
    if len(page.canonical)!=1 or not page.canonical[0].startswith(ORIGIN+'/'):errors.append(f'Invalid canonical: {path}')
    for href in page.links:
        if not href or href=='#':errors.append(f'Empty link: {path}')
        url=urlparse(urljoin(pageurl,href))
        if url.scheme not in ('http','https'):continue
        if url.netloc.lower()!=urlparse(ORIGIN).netloc:
            external.add(href);continue
        internal+=1;target=route(url.path)
        if not target.exists():errors.append(f'Missing target: {path.relative_to(OUT)} -> {href}')
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:errors.append(f'Missing anchor: {href}')
    body=' '.join(page.text)
    for sample in ['Your Name','GitHub University','Paper Title Number','fourth-year','UA-111540567','TODO']:
        if sample in body:errors.append(f'Stale/sample content {sample}: {path}')
for name in ['docs','local','scripts','licenses','vendor','_data','_pages','Gemfile','Gemfile.lock','README.md','THIRD_PARTY_NOTICES.md']:
    if (OUT/name).exists():errors.append(f'Internal material in output: {name}')
for p in (ROOT/'files').glob('*'):
    target=OUT/'files'/p.name
    if p.is_file() and (not target.exists() or hashlib.sha256(p.read_bytes()).digest()!=hashlib.sha256(target.read_bytes()).digest()):errors.append(f'Changed/missing legacy resource: {p.name}')
for url in ['/','/publications/','/cv/','/about/','/about.html','/resume/','/resume','/MeilongXu_Resume.pdf']:
    if not route(url).exists():errors.append(f'Missing compatibility route: {url}')
if (ROOT/'MeilongXu_Resume.pdf').read_bytes()!=(OUT/'MeilongXu_Resume.pdf').read_bytes():errors.append('CV differs from supplied PDF')
home=pages[OUT/'index.html'];allpubs=pages[OUT/'publications/index.html']
if len(home.articles)!=8 or len(allpubs.articles)!=12:errors.append('Unexpected publication count')
for term in ['Ph.D. Candidate','May 2027','Research Scientist','Applied Scientist','Machine Learning Engineer','ECCV 2026','(TMI) 2026','Topo-R1','Academic Service']:
    if term not in ' '.join(home.text):errors.append(f'Missing required content: {term}')
for p in [OUT/'sitemap.xml',OUT/'robots.txt']:
    txt=p.read_text()
    if 'localhost' in txt or '127.0.0.1' in txt:errors.append(f'Local URL leaked: {p.name}')
report={'html_pages':len(pages),'internal_links_checked':internal,'unique_external_links':len(external),'selected_publications':len(home.articles),'all_publications':len(allpubs.articles),'errors':errors}
print(json.dumps(report,indent=2,ensure_ascii=False))
(ROOT/'local').mkdir(exist_ok=True)
(ROOT/'local/site-check.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
(ROOT/'local/external-links.json').write_text(json.dumps(sorted(external),indent=2))
sys.exit(bool(errors))
