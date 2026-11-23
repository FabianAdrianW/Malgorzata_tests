/* AM Flowers · suwak przejścia. Bez zależności.
   <div class="am-swipe" data-href="https://amflowers.pl/" data-asset-base="am/"></div>
   Linki z atrybutem data-am-go (np. do sklepu AM Flowers) też uruchamiają kurtynę.
   Docelowa strona dostaje ?z=malgorzata, żeby otworzyć się z rozsuwaną kurtyną (działa między domenami). */
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const THRESHOLD = 0.6;
  const wait = ms => new Promise(r => setTimeout(r, ms));

  function build(root) {
    const href = root.dataset.href || 'https://amflowers.pl/';
    const base = root.dataset.assetBase || '';
    root.innerHTML = `
      <p class="am-swipe__label" id="am-swipe-l">Kwiaciarnia Małgorzata rośnie</p>
      <div class="am-swipe__track">
        <svg class="am-swipe__cap l" viewBox="0 0 40 40" aria-hidden="true"><path d="M8 14.5l4.5 5.5-4.5 5.5-4.5-5.5z" class="d"/><path d="M40 16.5H27c-4 0-5.5-2.5-5.5-7M40 23.5H27c-4 0-5.5 2.5-5.5 7"/></svg>
        <span class="am-swipe__rail" aria-hidden="true"><span class="am-swipe__fill"></span></span>
        <svg class="am-swipe__cap r" viewBox="0 0 40 40" aria-hidden="true"><path d="M32 14.5l4.5 5.5-4.5 5.5-4.5-5.5z" class="d"/><path d="M0 16.5h13c4 0 5.5-2.5 5.5-7M0 23.5h13c4 0 5.5 2.5 5.5 7"/></svg>
        <span class="am-swipe__hint" aria-hidden="true">Przeciągnij do AM Flowers</span>
        <button class="am-swipe__handle" type="button" role="slider" aria-labelledby="am-swipe-l" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" aria-valuetext="Przeciągnij w prawo albo naciśnij Enter, aby przejść do AM Flowers">
          <svg viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="44" class="o"/><circle cx="50" cy="50" r="37" class="i"/><polygon points="50.0,23.0 54.0,40.3 69.1,30.9 59.7,46.0 77.0,50.0 59.7,54.0 69.1,69.1 54.0,59.7 50.0,77.0 46.0,59.7 30.9,69.1 40.3,54.0 23.0,50.0 40.3,46.0 30.9,30.9 46.0,40.3"/></svg>
        </button>
      </div>
      <a class="am-swipe__link" href="${href}">Albo przejdź zwykłym linkiem: AM Flowers</a>`;
    const track = root.querySelector('.am-swipe__track');
    const handle = root.querySelector('.am-swipe__handle');
    let p = 0, dragging = false, startX = 0, startP = 0, done = false;

    const span = () => track.clientWidth - handle.offsetWidth - 2 * handle.offsetLeft;
    const setW = () => root.style.setProperty('--span', span() + 'px');
    setW(); new ResizeObserver(setW).observe(track);
    const set = v => { p = Math.max(0, Math.min(1, v)); root.style.setProperty('--p', p.toFixed(4)); handle.setAttribute('aria-valuenow', Math.round(p * 100)); };
    const back = () => { root.classList.add('is-back'); set(0); setTimeout(() => root.classList.remove('is-back'), 460); };
    const finish = () => {
      if (done) return; done = true;
      root.classList.add('is-done'); set(1);
      go(href, base, handle);
    };

    handle.addEventListener('pointerdown', e => {
      if (done) return;
      dragging = true; startX = e.clientX; startP = p;
      handle.setPointerCapture(e.pointerId); root.classList.remove('is-back');
    });
    handle.addEventListener('pointermove', e => {
      if (!dragging) return;
      set(startP + (e.clientX - startX) / span());
    });
    const end = () => {
      if (!dragging) return; dragging = false;
      if (p === startP && p === 0) return finish();      // tap/click = przejście
      p >= THRESHOLD ? finish() : back();
    };
    handle.addEventListener('pointerup', end);
    handle.addEventListener('pointercancel', () => { dragging = false; back(); });
    handle.addEventListener('keydown', e => {
      if (done) return;
      if (e.key === 'Enter' || e.key === ' ' || e.key === 'End') { e.preventDefault(); finish(); }
      else if (e.key === 'ArrowRight' || e.key === 'ArrowUp') { e.preventDefault(); set(p + .1); if (p >= 1) finish(); }
      else if (e.key === 'ArrowLeft' || e.key === 'ArrowDown' || e.key === 'Home') { e.preventDefault(); set(e.key === 'Home' ? 0 : p - .1); }
    });
  }

  const mark = href => {
    try { const u = new URL(href, location.href); u.searchParams.set('z', 'malgorzata'); return u.href; } catch (_) { return href; }
  };
  let busy = false;
  async function go(href, base, handle) {
    if (busy) return; busy = true;
    try { sessionStorage.setItem('amArrive', '1'); } catch (_) {}
    href = mark(href);
    if (reduce) { location.href = href; return; }
    const r = handle.getBoundingClientRect();
    const ly = ((r.top + r.height / 2) / innerHeight * 100).toFixed(2) + '%';
    const ox = ((r.left + r.width / 2) / innerWidth * 100).toFixed(2) + '%';
    const c = document.createElement('div');
    c.className = 'am-curtain'; c.setAttribute('aria-hidden', 'true');
    c.style.setProperty('--ly', ly); c.style.setProperty('--ox', ox);
    c.innerHTML = `
      <div class="am-curtain__veil"><video muted playsinline autoplay loop preload="auto" poster="${base}img/curtain-poster.webp" src="${base}video/curtain.mp4"></video></div>
      <span class="am-curtain__line" style="top:calc(${ly} - 2.5px)"></span>
      <i class="am-curtain__c tl"></i><i class="am-curtain__c tr"></i><i class="am-curtain__c bl"></i><i class="am-curtain__c br"></i>
      <div class="am-curtain__mark"><img src="${base}logo/am-flowers-gold.svg" alt=""><p>Ta sam<b>AM</b>iłość do kwiatów.</p></div>`;
    document.body.appendChild(c);
    const link = document.createElement('link'); link.rel = 'prefetch'; link.href = href; document.head.appendChild(link);
    await wait(380); c.classList.add('s1');
    await wait(480); c.classList.add('s2');
    await wait(650); c.classList.add('s3');
    await wait(1100); location.href = href;
  }

  document.querySelectorAll('.am-swipe').forEach(build);

  /* zwykłe linki do AM Flowers: ta sama kurtyna */
  document.addEventListener('click', e => {
    const a = e.target.closest('a[data-am-go]');
    if (!a || e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || a.target === '_blank') return;
    e.preventDefault();
    const base = (document.querySelector('.am-swipe') || {}).dataset?.assetBase ?? a.dataset.amGo ?? '';
    go(a.href, base, a);
  });
  window.AMSwipe = { go: (href, el) => go(href, (document.querySelector('.am-swipe') || {}).dataset?.assetBase || '', el || document.body) };
})();
