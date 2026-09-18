// A tall sidebar always stays in normal document flow.
(() => {
  const sidebar = document.querySelector('.sidebar');
  if (!sidebar) return;
  const update = () => {
    sidebar.classList.toggle('can-stick', window.innerWidth > 800 && sidebar.scrollHeight + 80 <= window.innerHeight);
  };
  new ResizeObserver(update).observe(sidebar);
  window.addEventListener('resize', update, { passive: true });
  update();
})();
