/* AM Flowers · suwak przejścia. Bez zależności.
   <div class="am-swipe" data-href="https://amflowers.pl/" data-asset-base="am/"></div>
   Linki z atrybutem data-am-go (np. do sklepu AM Flowers) też uruchamiają kurtynę.
   Docelowa strona dostaje ?z=malgorzata, żeby otworzyć się z rozsuwaną kurtyną (działa między domenami). */
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const THRESHOLD = 0.6;
  const wait = ms => new Promise(r => setTimeout(r, ms));
  const resets = [];
  let busy = false, run = 0;

  function build(root) {
    const href = root.dataset.href || 'https://amflowers.pl/';
    const base = root.dataset.assetBase || '';
    root.innerHTML = `
      <p class="am-swipe__label" id="am-swipe-l"><svg viewBox="0 0 110 110" aria-hidden="true"><circle cx="55" cy="55" r="44" fill="none" stroke="currentColor" stroke-width="4"/><path fill="currentColor" d="M55 28l4.6 15.9 14.5-8-8 14.5L82 55l-15.9 4.6 8 14.5-14.5-8L55 82l-4.6-15.9-14.5 8 8-14.5L28 55l15.9-4.6-8-14.5 14.5 8z"/></svg>Kwiaciarnia Małgorzata rośnie</p>
      <div class="am-swipe__track">
        <span class="am-swipe__fill" aria-hidden="true"></span>
        <span class="am-swipe__hint" aria-hidden="true">Przeciągnij do AM Flowers<i>→</i></span>
        <button class="am-swipe__handle" type="button" role="slider" aria-labelledby="am-swipe-l" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" aria-valuetext="Przeciągnij w prawo albo naciśnij Enter, aby przejść do AM Flowers">
          <img src="${base}logo/am-monogram-gold.svg" alt="" width="1233" height="720">
        </button>
      </div>
      <a class="am-swipe__link" href="${href}">Albo przejdź zwykłym linkiem: AM Flowers</a>`;
    const track = root.querySelector('.am-swipe__track');
    const handle = root.querySelector('.am-swipe__handle');
    let p = 0, dragging = false, startX = 0, startP = 0, done = false;

    const setW = () => root.style.setProperty('--w', track.clientWidth + 'px');
    setW(); new ResizeObserver(setW).observe(track);
    const set = v => { p = Math.max(0, Math.min(1, v)); root.style.setProperty('--p', p.toFixed(4)); handle.setAttribute('aria-valuenow', Math.round(p * 100)); };
    const back = () => { root.classList.add('is-back'); set(0); setTimeout(() => root.classList.remove('is-back'), 460); };
    const finish = () => {
      if (done) return; done = true;
      root.classList.add('is-done'); set(1);
      go(href, base, handle);
    };

    resets.push(() => { done = false; dragging = false; root.classList.remove('is-done', 'is-back'); set(0); });

    handle.addEventListener('pointerdown', e => {
      if (done) return;
      dragging = true; startX = e.clientX; startP = p;
      handle.setPointerCapture(e.pointerId); root.classList.remove('is-back');
    });
    handle.addEventListener('pointermove', e => {
      if (!dragging) return;
      const span = track.clientWidth - track.clientHeight;
      set(startP + (e.clientX - startX) / span);
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
  async function go(href, base, handle) {
    if (busy) return; busy = true;
    const id = ++run;
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
      <div class="am-curtain__mark"><img src="${base}logo/am-flowers-gold.svg" alt=""><p>Dwa pokolenia,<br><b>AM</b>iłość do kwiatów ta sama.</p></div>`;
    document.body.appendChild(c);
    const link = document.createElement('link'); link.rel = 'prefetch'; link.href = href; link.dataset.amPrefetch = ''; document.head.appendChild(link);
    for (const [ms, step] of [[380, 's1'], [480, 's2'], [650, 's3'], [1100, null]]) {
      await wait(ms); if (id !== run) return;
      step ? c.classList.add(step) : (location.href = href);
    }
  }

  document.querySelectorAll('.am-swipe').forEach(build);
  document.fonts?.load("400 1em 'AM Cormorant'", 'AMiłość ó').catch(() => {});

  /* "Wstecz" przywraca stronę z pamięci przeglądarki razem z kurtyną: zdejmujemy ją i zerujemy suwak */
  addEventListener('pageshow', e => {
    if (!e.persisted) return;
    run++; busy = false;
    document.querySelectorAll('.am-curtain, link[data-am-prefetch]').forEach(n => n.remove());
    resets.forEach(f => f());
  });

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
