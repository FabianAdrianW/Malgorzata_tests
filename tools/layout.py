"""Wspólne elementy stron: wskaźnik w menu (kropka = gdzie jesteś, pigułka = gdzie kursor),
burger na mobile, wspólna stopka, strony prawne. Uruchom: python3 tools/layout.py (po tools/mega.py)."""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
ARR = '<svg class="i" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

NAV_CSS = '''
/* ===== shared nav ===== */
.menu{position:relative}
.menu a{position:relative;z-index:1;background:none!important}
.menu a[aria-current],.menu a.is-active{color:var(--ink)}
.menu a::after{content:"";position:absolute;left:50%;bottom:2px;width:5px;height:5px;margin-left:-2.5px;border-radius:50%;background:var(--rose);transform:scale(0);transition:transform .45s cubic-bezier(.34,1.56,.64,1)}
.menu a[aria-current]::after,.menu a.is-active::after{transform:scale(1)}
.menu__pill{position:absolute;z-index:0;top:4px;left:0;height:calc(100% - 8px);width:0;border-radius:999px;background:var(--blush-2);opacity:0;pointer-events:none;
  transition:transform .45s var(--ease),width .45s var(--ease),opacity .3s var(--ease)}
.menu__pill.on{opacity:1}
.burger{display:none;width:44px;height:44px;border:0;border-radius:999px;background:transparent;color:inherit;cursor:pointer;position:relative}
.burger span{position:absolute;left:13px;right:13px;height:1.5px;background:currentColor;transition:transform .4s var(--ease),opacity .2s}
.burger span:nth-child(1){top:17px}.burger span:nth-child(2){top:22px}.burger span:nth-child(3){top:27px}
.burger[aria-expanded="true"] span:nth-child(1){transform:translateY(5px) rotate(45deg)}
.burger[aria-expanded="true"] span:nth-child(2){opacity:0}
.burger[aria-expanded="true"] span:nth-child(3){transform:translateY(-5px) rotate(-45deg)}
.nav__tel{display:inline-flex;align-items:center;gap:.45rem;padding:.5rem .8rem;border-radius:999px;text-decoration:none;font-weight:600;font-size:.92rem;min-height:44px;transition:background .25s}
.nav__tel:hover{background:var(--blush-2)}
@media (max-width:1140px){
  .menu{display:none!important}.burger{display:block}.menu__pill{display:none}
  .nav__tel span{display:none}
  .nav.is-open .menu{display:flex!important;position:fixed;inset:var(--nav-h) 0 auto 0;flex-direction:column;gap:0;margin:0;padding:1rem clamp(1rem,5vw,2.5rem) 2rem;background:var(--bg);border-bottom:1px solid var(--line);box-shadow:0 30px 40px -30px rgba(47,42,43,.3)}
  .nav.is-open .menu a{font:360 1.6rem/1.2 var(--f-display);color:var(--ink);padding:.8rem 0;border-radius:0;border-bottom:1px solid var(--line);animation:mIn .5s var(--ease) both}
  .nav.is-open .menu li:nth-child(2) a{animation-delay:.04s}.nav.is-open .menu li:nth-child(3) a{animation-delay:.08s}.nav.is-open .menu li:nth-child(4) a{animation-delay:.12s}.nav.is-open .menu li:nth-child(5) a{animation-delay:.16s}
  .nav.is-open .menu a::after{left:auto;right:0;top:50%;bottom:auto;margin:-2.5px 0 0}
}
@keyframes mIn{from{opacity:0;transform:translateY(8px)}}
@media (max-width:560px){.nav__in{gap:.5rem}.brand{min-width:0}.brand span{min-width:0}.brand b{font-size:.98rem;white-space:normal;line-height:1.1}.brand small{display:none}.nav__cta{gap:.25rem}.cartbtn{padding:.5rem .75rem}.nav__tel{padding:.5rem .6rem}}

/* ===== skala (mniejsza, spokojniejsza) ===== */
html{font-size:15px}
:root{--wrap:min(1120px,100% - clamp(2rem,6vw,5rem))}
h2{font-size:clamp(1.7rem,2.7vw,2.35rem)}
.hero h1{font-size:clamp(2.1rem,min(4.1vw,7svh),3.5rem)}
.order .order__head h2{font-size:clamp(1.7rem,2.7vw,2.35rem)}
.gal__word{font-size:clamp(4rem,min(14.5vw,25svh),12.5rem)}
.bigtel{font-size:clamp(2.2rem,4.4vw,3.4rem)}
.slide blockquote{font-size:clamp(1.15rem,1.9vw,1.6rem)}
.rating b{font-size:clamp(3rem,5vw,4rem)}
.head h1{font-size:clamp(2.1rem,4vw,3.1rem)}
.feat__cap b{font-size:clamp(1.3rem,2vw,1.7rem)}
.btn{min-height:44px;padding:.6rem 1.2rem}
.nav .btn,.cartbtn{min-height:40px}
.mega .mp__tel{font-size:1.9rem}
.foot__tel{font-size:1.4rem!important}
.doc h1{font-size:clamp(2rem,4vw,2.7rem)}

/* ===== shared footer ===== */
.foot{width:var(--wrap);margin:clamp(2.5rem,6vw,4rem) auto 0;padding:clamp(2rem,4vw,2.8rem) 0 1.4rem;border-top:1px solid var(--line);display:grid;grid-template-columns:1.4fr repeat(3,1fr);gap:2rem;font-size:.9rem}
.foot h3{font:600 .8rem/1 var(--f-text,"Instrument Sans",sans-serif);letter-spacing:.02em;color:var(--muted);margin:0 0 .9rem}
.foot ul{list-style:none;margin:0;padding:0;display:grid;gap:.45rem}
.foot a{color:var(--ink);text-decoration:none;background:linear-gradient(currentColor,currentColor) 0 100%/0 1px no-repeat;transition:background-size .4s var(--ease)}
.foot a:hover{background-size:100% 1px}
.foot__brand{display:flex;flex-direction:column;gap:.7rem}
.foot__brand b{font:400 1.35rem/1.1 var(--f-display,"Fraunces",serif)}
.foot__brand p{color:var(--muted);max-width:32ch;margin:0}
.foot__tel{font:300 1.6rem/1 var(--f-display,"Fraunces",serif)!important;letter-spacing:-.02em}
.foot__bottom{grid-column:1/-1;display:flex;justify-content:space-between;flex-wrap:wrap;gap:.6rem;padding-top:1.2rem;border-top:1px solid var(--line);color:var(--muted);font-size:.8rem}
@media (max-width:860px){.foot{grid-template-columns:1fr 1fr}.foot__brand{grid-column:1/-1}}
@media (max-width:560px){.foot{grid-template-columns:1fr}}
'''

NAV_JS = '''
/* ===== shared nav: pill follows the cursor, dot marks the current place ===== */
(()=>{const nav=document.querySelector('.nav'),menu=nav&&nav.querySelector('.menu');if(!menu)return;
  let pill=menu.querySelector('.menu__pill');if(!pill){pill=document.createElement('li');pill.className='menu__pill';pill.setAttribute('aria-hidden','true');menu.appendChild(pill)}
  const links=[...menu.querySelectorAll('a')];
  const to=a=>{if(!a){pill.classList.remove('on');return}pill.style.width=a.offsetWidth+'px';pill.style.transform=`translateX(${a.offsetLeft}px)`;pill.classList.add('on')};
  links.forEach(a=>{a.addEventListener('mouseenter',()=>to(a));a.addEventListener('focus',()=>to(a))});
  const rest=()=>{const open=links.find(l=>l.classList.contains('is-open'));to(open||null)};
  menu.addEventListener('mouseleave',()=>setTimeout(rest,180));
  const mega=document.getElementById('mega');if(mega){mega.addEventListener('mouseleave',()=>setTimeout(rest,200));new MutationObserver(rest).observe(mega,{attributes:true,attributeFilter:['class']})}
  let bg=nav.querySelector('.burger');
  if(!bg){bg=document.createElement('button');bg.className='burger';bg.setAttribute('aria-expanded','false');bg.setAttribute('aria-label','Menu');bg.innerHTML='<span></span><span></span><span></span>';nav.querySelector('.nav__cta').appendChild(bg);
    bg.addEventListener('click',()=>{const o=nav.classList.toggle('is-open');bg.setAttribute('aria-expanded',o)});
    links.forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('is-open');bg.setAttribute('aria-expanded','false')}))}
})();
'''

def footer(home):
    h = lambda a: f'{home}{a}'
    return f'''<footer class="foot">
  <div class="foot__brand"><b>Kwiaciarnia Małgorzata</b><p>Bukiety, kompozycje i&nbsp;dekoracje układane ręcznie w&nbsp;Oławie.</p><a class="foot__tel" href="tel:+48570740729">570 740 729</a><a class="am-sig-foot" data-am-go href="https://fabianadrianw.github.io/AM_flowers/"><img src="am/logo/am-monogram-gold.svg" alt="" width="1233" height="720">Kwiaciarnia Małgorzata rośnie: poznaj AM Flowers</a></div>
  <div><h3>Strona</h3><ul><li><a href="{h('#zamow')}">Zamów bukiet</a></li><li><a data-am-go href="https://fabianadrianw.github.io/AM_flowers/sklep.html">Sklep</a></li><li><a href="{h('#sluby')}">Śluby i dekoracje</a></li><li><a href="{h('#oferta')}">Galeria</a></li><li><a href="{h('#opinie')}">Opinie</a></li></ul></div>
  <div><h3>Kontakt</h3><ul><li>ul. Jarosława Iwaszkiewicza 137A</li><li>55-200 Oława</li><li><a href="https://www.google.com/maps/search/?api=1&amp;query=Kwiaciarnia+Ma%C5%82gorzata+Iwaszkiewicza+137A+O%C5%82awa" target="_blank" rel="noopener">Wyznacz trasę</a></li><li><a href="https://www.facebook.com/kwiaciarniamalgorzata" target="_blank" rel="noopener">Facebook</a></li></ul></div>
  <div><h3>Informacje</h3><ul><li><a data-am-go href="https://fabianadrianw.github.io/AM_flowers/regulamin.html">Regulamin sklepu (AM Flowers)</a></li><li><a href="polityka-prywatnosci.html">Polityka prywatności</a></li><li><a data-am-go href="https://fabianadrianw.github.io/AM_flowers/">AM Flowers</a></li></ul></div>
  <div class="foot__bottom"><span>© 2026 Kwiaciarnia Małgorzata · AM Flowers, Oława</span><span>Strona: Adrian Wojtasik</span></div>
</footer>'''

def strip(s):
    s = re.sub(r'\n/\* ===== shared nav ===== \*/.*?(?=\n/\* ===== mega menu|</style>)', '', s, flags=re.S)
    s = re.sub(r'<script>\n/\* ===== shared nav: .*?</script>\n', '', s, flags=re.S)
    s = re.sub(r'<footer class="foot">.*?</footer>', '', s, flags=re.S)
    return s

def inject(name, home, footer_anchor):
    p = ROOT / name; s = strip(p.read_text())
    s = s.replace('</style>', NAV_CSS + '</style>', 1)
    s = s.replace('</body>', '<script>' + NAV_JS + '</script>\n</body>', 1)
    s = s.replace(footer_anchor, footer(home) + '\n' + footer_anchor, 1)
    p.write_text(s)

if __name__ == '__main__':
    inject('index.html', '', '<div class="bar"')
    if (ROOT / 'sklep.html').exists():
        inject('sklep.html', 'index.html', '\n<div class="scrim"')
    for n in ['regulamin.html', 'polityka-prywatnosci.html']:
        if (ROOT / n).exists():
            inject(n, 'index.html', '</body>')
    print('ok')
