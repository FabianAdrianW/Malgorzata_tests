# Kwiaciarnia Małgorzata, Oława (wersja testowa z przejściem do AM Flowers)

Kopia strony Kwiaciarni Małgorzata z repo `Kwiaciarnia_malgorzata` plus **faza 1 przejścia na markę AM Flowers**.

## Dwie domeny, jedna marka
- **Kwiaciarnia Małgorzata** (ta strona): klasyczna wizytówka dla stałych klientów. Galeria, szybkie zamówienie u florystki, śluby, opinie, kontakt. Bez sklepu i bez kwiatomatu.
- **AM Flowers** (`amflowers.pl`, repo `AM_flowers`): nowa marka premium. Sklep online, kwiatomat 24/7, historia mamy i córki.
- Łączy je **suwak przejścia** w hero oraz każdy link do AM Flowers (sklep, regulamin, stopka). Kliknięcie albo przeciągnięcie uruchamia szmaragdową kurtynę, a AM Flowers otwiera się z rozsuwaną kurtyną (parametr `?z=malgorzata`, działa między domenami).

## Co zmieniono względem `Kwiaciarnia_malgorzata`
| Zmiana | Gdzie |
|---|---|
| Podpis „AM Flowers” ze złotym monogramem pod nazwą w nagłówku | `index.html`, `polityka-prywatnosci.html` |
| Suwak przejścia w hero | `index.html`, `am/` |
| „Sklep”, „Zamów bukiet”, „Zamów podobny”, polecane bukiety prowadzą do sklepu AM Flowers (z kurtyną) | `index.html` |
| Stopka: link „Kwiaciarnia Małgorzata rośnie: poznaj AM Flowers”, © z obiema nazwami, regulamin sklepu u AM Flowers | stopka |
| Szybkie zamówienie wysyłane do `https://amflowers.pl/api/order` (CORS: `ALLOWED_ORIGINS` w AM Flowers); bez tego otwiera SMS | `index.html` |
| Usunięte: `sklep.html`, `sukces.html`, `regulamin.html`, funkcja Netlify, `netlify.toml`, `package.json` | sklep jest w AM Flowers |
| Hosting w polityce prywatności: Cloudflare zamiast Netlify | `polityka-prywatnosci.html` |

## Pliki
- `am/`: moduł suwaka (`am-swipe.css`, `am-swipe.js`), logo, wideo kurtyny. Kopia z repo `AM_flowers/swipe`.
- `tools/am_link.py`: wprowadza fazę 1. Adres AM Flowers zmienia się w jednym miejscu (`AM = 'https://amflowers.pl/'`), potem uruchom skrypt ponownie.
- `tools/mega.py`, `tools/layout.py`: jak wcześniej; po ich uruchomieniu uruchom też `tools/am_link.py`.

## Wdrożenie
Cloudflare Pages, statycznie (bez kroku budowania). Własna domena kwiaciarni. Do testów przed podpięciem domen ustaw w `tools/am_link.py` adres testowy AM Flowers (np. `https://am-flowers.pages.dev/`) i uruchom skrypt.

## Do uzupełnienia
- Adres: na stronie 137A, na wizytówce 137B. Potwierdzić.
- Docelowe domeny obu stron.
- Faza 2 (za 3–6 miesięcy): wspólny znak `am/logo/lockup-am-x-malgorzata.svg` zamiast obecnego logo.
