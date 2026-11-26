"""Faza 1 przejścia na AM Flowers (jednorazowo, po mega.py i layout.py):
podpis AM Flowers przy logo i w stopce, suwak w hero, sklep i regulamin prowadzą do AM Flowers (z kurtyną)."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parent.parent
AM = 'https://fabianadrianw.github.io/AM_flowers/'   # jedno miejsce do zmiany adresu AM Flowers

REPL = [
    ('href="sklep.html', f'data-am-go href="{AM}sklep.html'),
    ("$('#lbShop').href='sklep.html#p='", f"$('#lbShop').href='{AM}sklep.html#p='"),
    ('<li><a href="regulamin.html">Regulamin sklepu</a></li>', f'<li><a data-am-go href="{AM}regulamin.html">Regulamin sklepu (AM Flowers)</a></li>'),
    ('<li>Płatności: BLIK, karta, Przelewy24</li>', f'<li><a data-am-go href="{AM}">AM Flowers</a></li>'),
    ('<span><b>Kwiaciarnia Małgorzata</b><small>Oława</small></span>',
     '<span><b>Kwiaciarnia Małgorzata</b><small class="am-sig"><img src="am/logo/am-monogram-gold.svg" alt="" width="1233" height="720">AM Flowers</small></span>'),
    ('<a class="foot__tel" href="tel:+48570740729">570 740 729</a></div>',
     f'<a class="foot__tel" href="tel:+48570740729">570 740 729</a><a class="am-sig-foot" data-am-go href="{AM}"><img src="am/logo/am-monogram-gold.svg" alt="" width="1233" height="720">Kwiaciarnia Małgorzata rośnie: poznaj AM Flowers</a></div>'),
    ('© 2026 Kwiaciarnia Małgorzata, Oława', '© 2026 Kwiaciarnia Małgorzata · AM Flowers, Oława'),
    ('<small class="menu__desc">Zamów online z odbiorem lub dostawą</small>', '<small class="menu__desc">Zamów online w AM Flowers</small>'),
]

CSS = '''
/* ===== AM Flowers: podpis i suwak (faza 1) ===== */
.brand small.am-sig{display:flex;align-items:center;gap:.3rem;color:#7A5A22;letter-spacing:.14em;text-transform:uppercase;font-size:.62rem;font-weight:600}
.brand small.am-sig img{width:auto;height:11px;border-radius:0;box-shadow:none;background:none;object-fit:contain}
@media (max-width:560px){.brand small.am-sig{display:flex}}
.am-sig-foot{display:inline-flex;align-items:center;gap:.5rem;margin-top:.4rem;font-size:.85rem;color:#7A5A22!important}
.am-sig-foot img{height:14px;width:auto}
.hero .am-swipe{margin-top:1.8rem}
'''

def patch(path, html=True):
    p = ROOT / path
    if not p.exists():
        return
    s = p.read_text()
    for a, b in REPL:
        if b not in s:
            s = s.replace(a, b)
    if html and 'am/am-swipe.css?v=4' not in s:
        s = s.replace('</style>', CSS + '</style>', 1)
        s = s.replace('</head>', '<link rel="stylesheet" href="am/am-swipe.css?v=4">\n</head>', 1)
        s = s.replace('</body>', '<script src="am/am-swipe.js?v=4" defer></script>\n</body>', 1)
    p.write_text(s)

if __name__ == '__main__':
    for n in ['index.html', 'polityka-prywatnosci.html']:
        patch(n)
    # suwak w hero strony głównej
    p = ROOT / 'index.html'; s = p.read_text()
    if 'class="am-swipe"' not in s:
        s = re.sub(r'(<ul class="facts" data-reveal="3">.*?</ul>)',
                   lambda m: m.group(1) + f'\n      <div class="am-swipe" data-href="{AM}" data-asset-base="am/" data-reveal="3"></div>', s, count=1, flags=re.S)
    p.write_text(s)
    # generatory: te same zmiany, żeby kolejne uruchomienie ich nie cofnęło
    for n in ['tools/layout.py', 'tools/mega.py']:
        patch(n, html=False)
    print('ok')
