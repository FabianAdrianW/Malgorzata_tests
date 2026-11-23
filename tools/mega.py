"""Wstawia mega-menu (rozwijane panele w navbarze) do index.html i sklep.html.
Uruchom ponownie po zmianie treści paneli: python3 tools/mega.py"""
import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
STAR = '<svg viewBox="0 0 20 20"><path d="M10 1.5l2.6 5.4 5.9.8-4.3 4.1 1 5.9L10 15l-5.2 2.7 1-5.9L1.5 7.7l5.9-.8z"/></svg>'
ARR = '<svg class="i" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

def panels(home):  # home = '' on index, 'index.html' on other pages
    h = lambda a: f'{home}{a}'
    return f'''
<div class="mega" id="mega" aria-hidden="true">
  <div class="mega__box"><span class="mega__tip" aria-hidden="true"></span>
  <div class="mega__track">
    <section class="mp" data-p="oferta" aria-label="Galeria">
      <div class="mp__text"><b class="mp__h">Galeria</b><p>Bukiety, kompozycje i&nbsp;dekoracje z&nbsp;naszej pracowni. Każde zdjęcie można powiększyć.</p>
        <a class="mp__more" href="{h('#oferta')}">Otwórz galerię{ARR}</a></div>
      <div class="mp__thumbs">
        <a href="{h('#oferta')}" class="mp__th"><img src="img/p09.webp" alt="" loading="lazy"><span>Pastele</span></a>
        <a href="{h('#oferta')}" class="mp__th"><img src="img/p10.webp" alt="" loading="lazy"><span>Czerwienie</span></a>
        <a href="{h('#oferta')}" class="mp__th"><img src="img/p01.webp" alt="" loading="lazy"><span>Śluby</span></a>
      </div>
    </section>
    <section class="mp mp--shop" data-p="sklep" aria-label="Sklep">
      <div class="mp__list">
        <a data-am-go href="https://fabianadrianw.github.io/AM_flowers/sklep.html#kat=bukiety" class="mp__item"><img src="img/p16.webp" alt="" loading="lazy"><span><b>Bukiety</b><small>Na każdą okazję, w&nbsp;3&nbsp;wielkościach</small></span></a>
        <a data-am-go href="https://fabianadrianw.github.io/AM_flowers/sklep.html#kat=kompozycje" class="mp__item"><img src="img/p04.webp" alt="" loading="lazy"><span><b>Kompozycje</b><small>Ślubne i&nbsp;dekoracyjne, na zamówienie</small></span></a>
        <a data-am-go href="https://fabianadrianw.github.io/AM_flowers/sklep.html#kat=pamiec" class="mp__item"><img src="img/p13.webp" alt="" loading="lazy"><span><b>Pamięć</b><small>Wieńce i&nbsp;kompozycje nagrobne</small></span></a>
        <a data-am-go href="https://fabianadrianw.github.io/AM_flowers/sklep.html" class="mp__more">Cały sklep{ARR}</a>
      </div>
      <a data-am-go href="https://fabianadrianw.github.io/AM_flowers/sklep.html#p=pastelowy" class="mp__feat"><img src="img/p09.webp" alt="" loading="lazy"><span class="mp__badge">Bestseller</span><span class="mp__cap"><b>Bukiet Pastelowy</b><small>od 189 zł · BLIK, karta albo przy odbiorze</small></span></a>
    </section>
    <section class="mp" data-p="sluby" aria-label="Śluby i dekoracje">
      <div class="mp__list">
        <a href="{h('#sluby')}" class="mp__row"><b>Wiązanki ślubne i&nbsp;wianki</b><small>Dobrane do sukni i&nbsp;kolorów wesela</small></a>
        <a href="{h('#sluby')}" class="mp__row"><b>Dekoracje kościołów</b><small>Ławki, ołtarz, wejście, także plener</small></a>
        <a href="{h('#sluby')}" class="mp__row"><b>Dekoracje sal</b><small>Stoły, lasy w&nbsp;szkle, balony z&nbsp;helem</small></a>
        <a href="tel:+48570740729" class="mp__more">Umów rozmowę: 570 740 729{ARR}</a>
      </div>
      <a href="{h('#sluby')}" class="mp__feat mp__feat--tall"><img src="img/slub-wiazanka.webp" alt="" loading="lazy"></a>
    </section>
    <section class="mp mp--small" data-p="opinie" aria-label="Opinie">
      <div class="mp__rate"><b>4,5</b><span class="mp__stars" aria-label="4,5 na 5">{STAR*4}<span style="opacity:.35">{STAR}</span></span><small>148 opinii w&nbsp;Google</small></div>
      <blockquote class="mp__quote">„Najpiękniejsze kompozycje, uwielbiam patrzeć jak Panie tworzą bukiet jakby malowały dzieło sztuki”<small>Pamela Kwak, Google</small></blockquote>
      <a class="mp__more" href="{h('#opinie')}">Przeczytaj opinie{ARR}</a>
    </section>
    <section class="mp mp--small" data-p="kontakt" aria-label="Kontakt">
      <a class="mp__tel" href="tel:+48570740729">570 740 729</a>
      <p class="mp__addr">ul. Jarosława Iwaszkiewicza 137A<br>55-200 Oława</p>
      <div class="mp__btns"><a class="mp__more" href="https://www.google.com/maps/search/?api=1&amp;query=Kwiaciarnia+Ma%C5%82gorzata+Iwaszkiewicza+137A+O%C5%82awa" target="_blank" rel="noopener">Wyznacz trasę{ARR}</a>
        <a class="mp__more" href="https://www.facebook.com/kwiaciarniamalgorzata" target="_blank" rel="noopener">Facebook{ARR}</a></div>
    </section>
  </div></div>
</div>'''

DESCS = {'oferta': 'Nasze bukiety i dekoracje', 'sklep': 'Zamów online z odbiorem lub dostawą',
         'sluby': 'Wiązanki, kościoły, sale', 'opinie': '4,5 w Google, 148 opinii', 'kontakt': 'Oława, Iwaszkiewicza 137A'}

CSS = '''
/* ===== mega menu ===== */
.menu a .menu__desc{display:none}
.mega{position:absolute;left:0;top:calc(var(--nav-h) - 6px);z-index:49;pointer-events:none;width:0}
.mega__box{position:absolute;left:0;top:0;width:var(--mw,560px);height:var(--mh,240px);transform:translateX(var(--mx,0px)) translateY(8px) scale(.98);transform-origin:var(--mo,50%) 0;
  background:var(--surface);border-radius:20px;box-shadow:0 30px 60px -30px rgba(47,42,43,.45),0 0 0 1px var(--line);opacity:0;overflow:hidden;
  transition:opacity .25s var(--ease),transform .45s var(--ease),width .45s var(--ease),height .45s var(--ease)}
.mega.on{pointer-events:auto}
.mega.on .mega__box{opacity:1;transform:translateX(var(--mx,0px)) translateY(0) scale(1)}
.mega.instant .mega__box{transition:opacity .25s var(--ease),transform .45s var(--ease)}
.mega__tip{position:absolute;top:-6px;left:var(--tx,50%);width:12px;height:12px;background:var(--surface);transform:rotate(45deg);transition:left .45s var(--ease);box-shadow:-1px -1px 0 var(--line)}
.mega__track{position:relative;width:100%;height:100%}
.mp{position:absolute;left:0;top:0;padding:1.2rem;display:grid;gap:1.2rem;opacity:0;visibility:hidden;transform:translateX(var(--from,0px));
  transition:opacity .3s var(--ease),transform .45s var(--ease),visibility 0s .45s}
.mp.on{opacity:1;visibility:visible;transform:none;transition:opacity .35s .05s var(--ease),transform .45s var(--ease),visibility 0s}
.mp>*,.mp__list>*,.mp__thumbs>*{opacity:0;transform:translateY(6px);transition:opacity .4s var(--ease),transform .5s var(--ease)}
.mp.on>*,.mp.on .mp__list>*,.mp.on .mp__thumbs>*{opacity:1;transform:none}
.mp.on .mp__list>*:nth-child(2),.mp.on .mp__thumbs>*:nth-child(2){transition-delay:.05s}
.mp.on .mp__list>*:nth-child(3),.mp.on .mp__thumbs>*:nth-child(3){transition-delay:.1s}
.mp.on .mp__list>*:nth-child(4){transition-delay:.15s}
.mp[data-p="oferta"]{grid-template-columns:200px auto;width:620px}
.mp--shop,.mp[data-p="sluby"]{grid-template-columns:300px 210px;width:560px}
.mp--small{width:320px;gap:.9rem}
.mp__h{display:block;font:400 1.35rem/1.1 var(--f-display);margin-bottom:.4rem}
.mp p,.mp small{font-size:.84rem;color:var(--muted)}
.mp a{text-decoration:none;color:inherit}
.mp__text{display:flex;flex-direction:column;justify-content:space-between;gap:.8rem;padding:.3rem 0}
.mp__more{display:inline-flex;align-items:center;gap:.35rem;font-weight:600;font-size:.85rem;color:var(--rose)!important;min-height:36px}
.mp__more svg{width:16px;height:16px;transition:transform .35s var(--ease)}
.mp__more:hover svg{transform:translateX(4px)}
.mp__thumbs{display:grid;grid-template-columns:repeat(3,120px);gap:.6rem}
.mp__th{position:relative;display:block;aspect-ratio:3/4;border-radius:12px;overflow:hidden;background:var(--blush)}
.mp__th img,.mp__item img,.mp__feat img{width:100%;height:100%;object-fit:cover;transition:transform .8s var(--ease)}
.mp__th span{position:absolute;left:.5rem;bottom:.45rem;color:#fff;font:italic 360 .9rem var(--f-display);text-shadow:0 1px 8px rgba(0,0,0,.5)}
.mp__th:hover img,.mp__item:hover img,.mp__feat:hover img{transform:scale(1.07)}
.mp__list{display:flex;flex-direction:column;gap:.2rem}
.mp__item{display:grid;grid-template-columns:52px 1fr;gap:.8rem;align-items:center;padding:.45rem;border-radius:12px;transition:background-color .25s var(--ease)}
.mp__item img{width:52px;height:52px;border-radius:10px}
.mp__item:hover,.mp__row:hover{background:var(--blush-2)}
.mp__item b,.mp__row b{display:block;font-weight:600;font-size:.92rem}
.mp__item small,.mp__row small{display:block;margin-top:.05rem}
.mp__row{display:block;padding:.6rem .7rem;border-radius:12px;transition:background-color .25s var(--ease)}
.mp__list .mp__more{padding-left:.7rem}
.mp__feat{position:relative;display:block;border-radius:14px;overflow:hidden;background:var(--blush);min-height:230px}
.mp__badge{position:absolute;left:.6rem;top:.6rem;background:var(--rose);color:#fff;border-radius:999px;padding:.2rem .6rem;font-size:.72rem;font-weight:600}
.mp__cap{position:absolute;left:0;right:0;bottom:0;padding:2rem .8rem .7rem;background:linear-gradient(180deg,transparent,rgba(27,23,24,.7));color:#fff}
.mp__cap b{display:block;font:400 1.05rem var(--f-display)}.mp__cap small{color:rgba(255,255,255,.85);font-size:.76rem}
.mp__rate{display:flex;align-items:center;gap:.7rem;flex-wrap:wrap}
.mp__rate b{font:300 2.8rem/1 var(--f-display);letter-spacing:-.04em}
.mp__stars{display:inline-flex;color:var(--rose)}.mp__stars svg{width:15px;height:15px;fill:currentColor}
.mp__rate small{width:100%}
.mp__quote{margin:0;font:italic 360 1rem/1.45 var(--f-display);padding:.8rem .9rem;border-radius:12px;background:var(--blush-2)}
.mp__quote small{display:block;margin-top:.4rem;font:400 .76rem var(--f-text)}
.mp__tel{font:300 2.2rem/1 var(--f-display);letter-spacing:-.03em;transition:color .25s}
.mp__tel:hover{color:var(--rose)}
.mp__addr{font-size:.9rem!important;color:var(--ink)!important}
.mp__btns{display:flex;gap:1rem;flex-wrap:wrap}
.menu a .menu__chev{display:inline-block;width:10px;height:10px;margin-left:.3rem;vertical-align:.05em;opacity:.5;transition:transform .35s var(--ease),opacity .25s}
.menu a.is-open .menu__chev{transform:rotate(180deg);opacity:1}
@media (max-width:1140px){
  .mega{display:none}.menu a .menu__chev{display:none}
  .nav.is-open .menu a .menu__desc{display:block;font:400 .8rem/1.3 var(--f-text);color:var(--muted);margin-top:.15rem;letter-spacing:0}
}
@media (prefers-reduced-motion:reduce){.mega__box,.mp,.mp>*{transition:none!important}}
'''

JS = '''
/* ===== mega menu ===== */
(()=>{const nav=document.querySelector('.nav'),mega=document.getElementById('mega');if(!mega)return;
  const box=mega.querySelector('.mega__box'),panels=[...mega.querySelectorAll('.mp')];
  const links=[...document.querySelectorAll('.menu a[data-mega]')];let cur=null,t=null,curIdx=-1;
  const order=links.map(a=>a.dataset.mega);
  function open(a){clearTimeout(t);const id=a.dataset.mega,p=panels.find(x=>x.dataset.p===id);if(!p||matchMedia('(max-width:1140px)').matches)return;
    const idx=order.indexOf(id);const first=!mega.classList.contains('on');
    panels.forEach(x=>{if(x!==p){x.style.setProperty('--from',(idx>curIdx?-40:40)+'px');x.classList.remove('on')}});
    p.style.setProperty('--from',first?'0px':(idx>curIdx?40:-40)+'px');
    const w=p.offsetWidth,h=p.offsetHeight,nr=nav.getBoundingClientRect(),ar=a.getBoundingClientRect();
    let x=ar.left+ar.width/2-w/2-nr.left;x=Math.max(16,Math.min(x,nr.width-w-16));
    mega.classList.toggle('instant',first);
    box.style.setProperty('--mw',w+'px');box.style.setProperty('--mh',h+'px');box.style.setProperty('--mx',x+'px');
    box.style.setProperty('--tx',(ar.left+ar.width/2-nr.left-x-6)+'px');box.style.setProperty('--mo',(ar.left+ar.width/2-nr.left-x)+'px');
    requestAnimationFrame(()=>{p.classList.add('on');mega.classList.add('on');mega.setAttribute('aria-hidden','false')});
    links.forEach(l=>{l.classList.toggle('is-open',l===a);l.setAttribute('aria-expanded',l===a)});cur=a;curIdx=idx}
  function close(){t=setTimeout(()=>{mega.classList.remove('on');mega.setAttribute('aria-hidden','true');panels.forEach(x=>x.classList.remove('on'));
    links.forEach(l=>{l.classList.remove('is-open');l.setAttribute('aria-expanded','false')});cur=null;curIdx=-1},160)}
  links.forEach(a=>{a.setAttribute('aria-expanded','false');a.addEventListener('mouseenter',()=>open(a));a.addEventListener('focus',()=>open(a));a.addEventListener('mouseleave',close)});
  mega.addEventListener('mouseenter',()=>clearTimeout(t));mega.addEventListener('mouseleave',close);
  mega.addEventListener('focusin',()=>clearTimeout(t));mega.addEventListener('focusout',e=>{if(!mega.contains(e.relatedTarget)&&!links.includes(e.relatedTarget))close()});
  addEventListener('keydown',e=>{if(e.key==='Escape'&&cur){const c=cur;close();c.focus()}});
  mega.addEventListener('click',e=>{if(e.target.closest('a'))close()});
  addEventListener('scroll',()=>{if(cur&&scrollY>0&&!mega.matches(':hover'))close()},{passive:true});
})();
'''

CHEV = '<svg class="menu__chev" viewBox="0 0 10 10" aria-hidden="true"><path d="M2 3.5l3 3 3-3" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>'

def inject(path, home):
    s = path.read_text()
    s = re.sub(r'\n<div class="mega" id="mega".*?</section>\n  </div></div>\n</div>', '', s, flags=re.S)
    s = re.sub(r'/\* ===== mega menu ===== \*/.*?(?=</style>)', '', s, flags=re.S)
    s = re.sub(r'<script>\n/\* ===== mega menu ===== \*/\n\(\(\)=>\{.*?\n\}\)\(\);\n</script>\n?', '', s, flags=re.S)
    keymap = {'#oferta': 'oferta', 'https://fabianadrianw.github.io/AM_flowers/sklep.html': 'sklep', '#sluby': 'sluby', '#opinie': 'opinie', '#kontakt': 'kontakt'}
    def fix(m):
        href, rest, label = m.group(1), m.group(2), m.group(3)
        key = next((v for k, v in keymap.items() if href.endswith(k)), None)
        if not key:
            return m.group(0)
        label = re.sub(r'<svg class="menu__chev".*?</svg>|<small class="menu__desc">.*?</small>', '', label)
        rest = re.sub(r'\s*data-mega="\w+"', '', rest)
        return f'<li><a href="{href}"{rest} data-mega="{key}">{label}{CHEV}<small class="menu__desc">{DESCS[key]}</small></a></li>'
    a = s.index('<ul class="menu"'); b = s.index('</ul>', a)
    s = s[:a] + re.sub(r'<li><a href="([^"]+)"([^>]*)>(.*?)</a></li>', fix, s[a:b]) + s[b:]
    s = s.replace('</header>', panels(home) + '\n</header>', 1)
    s = s.replace('</style>', CSS + '</style>', 1)
    s = s.replace('</body>', '<script>' + JS + '</script>\n</body>', 1) if '<script>/* mega' not in s else s
    path.write_text(s)

if __name__ == '__main__':
    inject(ROOT / 'index.html', '')
    if (ROOT / 'sklep.html').exists():
        inject(ROOT / 'sklep.html', 'index.html')
    for n in ['regulamin.html', 'polityka-prywatnosci.html']:
        if (ROOT / n).exists():
            inject(ROOT / n, 'index.html')
    print('ok')
