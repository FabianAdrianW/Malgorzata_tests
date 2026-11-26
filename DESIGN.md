# Kwiaciarnia Małgorzata: DESIGN.md (v3, 2026-11-17)

## Kierunek
Profesjonalnie, minimalistycznie, wiosennie. Prawdziwe bukiety kwiaciarni grają główną rolę, a interfejs schodzi na drugi plan. Całość jest na jednym jasnym tle, bez widocznych granic sekcji. Rytm budują zdjęcia, zaokrąglone panele (zamówienie, kontakt) i wstążka między zamówieniem a ślubami.
Skala: odpowiednik dawnego zoomu 80% (tekst główny 16 px, nagłówki i odstępy mniejsze o ok. 20%).

## Paleta: Piwonia i szałwia
| Token | Hex | Rola |
|---|---|---|
| --bg | #FBF7F4 | tło całej strony |
| --surface | #FFFFFF | karty, pola, cytaty |
| --blush / --blush-2 | #F6E3E0 / #FBEEEB | pigułka w menu, panel zamówienia |
| --sage / --sage-2 | #B7C6AB / #E7EDE1 | detale, panel kontaktu, komunikat sukcesu |
| --leaf | #4E6346 | ikony |
| --ink | #2F2A2B | tekst |
| --muted | #6B6164 | tekst pomocniczy |
| --rose | #C24468 | jedyny kolor akcji (hover #A3304F) |
Bez trybu ciemnego (decyzja Fabiana).

## Typografia
Fraunces (300–440) do nagłówków, a kursywa w kolorze akcji pojawia się tylko w h1. Instrument Sans do tekstu. Oba kroje hostowane lokalnie, z latin-ext.

## Układ
1. Navbar (burger poniżej 1140 px): 64 px stałej wysokości, półprzezroczysty z rozmyciem. Logo po lewej, menu w środku, telefon i przycisk „Zamów bukiet” po prawej. Pod menu przesuwa się różowa pigułka (hover i aktywna sekcja), po przewinięciu pojawia się cienka linia.
2. Hero (v3.1): pełnoekranowe zdjęcie pastelowego bukietu (img/hero.webp, 1536 px) na prawych 60% ekranu, z lewej maska przechodząca w tło. Tekst po lewej. Przy scrollu zdjęcie lekko się przybliża (do 8%). Na mobile zdjęcie jest na górze i zanika ku dołowi.
3. Bukiety z pracowni: 3 kafle w asymetrycznej siatce z przesunięciami. Kliknięcie „Zamów podobny” wpisuje bukiet do uwag zamówienia. Pod kaflami 4 usługi w rzędzie.
4. Zamówienie (panel blush) w 3 krokach: wielkość (3 karty), termin i odbiór (przełączniki), telefon z przyciskiem. Szczegóły w rozwijanym „Dodaj szczegóły”. Na desktopie obok jest przyklejone podsumowanie.
5. Wstążka (grafika z wyciętym tłem) prowadzi do ślubów.
6. Śluby: tekst z listą i para zdjęć.
7. Pamięć: 3 zdjęcia, środkowe przesunięte.
8. Opinie: ocena 4,5 (przyklejona), 3 cytaty bez zmian.
9. Kontakt (panel sage): duży numer, adres, godziny, Facebook.

## Ruch
Delikatne wejście hero, pigułka w menu, przybliżenie zdjęć o 3,5% na hover, uniesienie kart. Nic się nie kołysze. Przy `prefers-reduced-motion` ruch jest wyłączony.

## Zamówienia
Formularz Netlify Forms (`name="zamowienie"`, honeypot). Na Netlify zgłoszenie trafia do panelu i na e-mail kwiaciarni (do ustawienia w Netlify). Bez Netlify formularz otwiera SMS z gotową treścią na 570 740 729.

## Zdjęcia
- p08–p16: bukiety kwiaciarni (FB, zgoda do potwierdzenia).
- p01, p04: kompozycje na stojakach (śluby, dekoracje).
- p05, p06, p13: nagrobki i wieńce.
- Uwaga: p01–p07 i p13 wyglądają na mocno przetworzone lub wygenerowane. Potwierdzić z kwiaciarnią, że to ich realizacje.
- Wygenerowane w Gemini: wstążka i akwarelowa gałązka (dekoracja).

## TODO
Logo w oryginale, zgoda na zdjęcia, ceny (79/129/199 zł robocze), godziny otwarcia, strefa i koszt dostawy, płatność przy odbiorze, „oddzwonimy”, e-mail do powiadomień Netlify, domena, podpis w stopce.

## Zmiany v3
- Każda sekcja mieści się w jednym ekranie (`--vh = 100svh - nav`). Wysokości zdjęć, hero i zamówienia liczone są od okna.
- Oferta to przypięta, pozioma galeria: scroll w dół przesuwa karty z prawej do lewej, zdjęcia mają lekką paralaksę, pod spodem jest pasek postępu. Na ekranach do 860 px jest natywne przewijanie palcem ze snapem. Sekcja „Pamięć” weszła do galerii.
- Przejścia: tło strony płynnie zmienia odcień (`data-tone`): #FBF7F4, #FBEEEB przy zamówieniu, #F7F1EE przy opiniach, #F1F3EC przy kontakcie. Treść sekcji wyłania się przy wejściu (`data-reveal`).
- Opinie: karta z oceną 4,5 i odznaką Google, obok duża opinia w karuzeli (auto co 7 s, pauza na hover lub focus, strzałki i kropki).
- Kontakt: zdjęcie p12 w tle panelu, przechodzące maską w kolor panelu.
- Zamówienie: wielkości w wierszach z miniaturą, data i adres pojawiają się w jednym wierszu.

## Zmiany v3.2
- „Co dla Ciebie ułożymy” zmienione na **Galerię**: 11 zdjęć przesuwa się samo, powoli (ok. 28 px/s), w nieskończonej pętli. Na hover lub focus galeria staje. Są strzałki (o jedno zdjęcie), przeciąganie myszą lub palcem i lightbox po kliknięciu (strzałki, Esc). Podpisy to rodzaje (bukiet, kompozycja ślubna, wieńce), bez przycisków akcji.
- Opinie: karta z oceną 4,5 nachodzi na duże zdjęcie bukietu (p16) w zaokrąglonym kadrze.

## Sklep (sklep.html, v1)
- Osobna strona, link „Sklep” w menu (zastąpił „Zamów online”). Sekcja zamówienia w 3 krokach na stronie głównej zostaje jako szybka ścieżka.
- Nagłówek z trzema obietnicami (płatność przy odbiorze, odbiór lub dostawa, bilecik gratis: do potwierdzenia). Przyklejony pasek: kategorie (Wszystkie / Bukiety / Kompozycje / Pamięć) z przesuwaną pigułką i sortowanie.
- Karty: zdjęcie 4:5, na hover drugie zdjęcie i wysuwane przyciski „Dodaj do koszyka” i „Szczegóły”. Pod kartą nazwa, cena i kropki kolorów.
- Karta produktu (modal, na mobile wysuwany od dołu): wielkość S/M/L (−30 / 0 / +60 zł), bilecik, ilość, dodanie do koszyka.
- Dodanie: miniatura „leci” do koszyka, licznik podskakuje, pojawia się toast. Koszyk zapisany w localStorage.
- Koszyk w szufladzie z prawej, w 3 krokach: koszyk, dane (kiedy, odbiór lub dostawa, imię, telefon, uwagi), potwierdzenie z animowanym checkiem. Wysyłka przez Netlify Forms (`sklep`), a bez Netlify przez SMS z gotową treścią.
- TODO: ceny i nazwy robocze, kategorie i oferta do potwierdzenia, flowerboxy (brak zdjęć).

## Zmiany v4 (2026-11-17)
- Galeria: wariant 5 „Litery jako okna”. Napis „Galeria” jest wypełniony stałym zdjęciem czerwonego bukietu (p10), które przy scrollu przesuwa się w literach. Napis odsłania się od góry przy wejściu. Pod nim 6 zdjęć: wejście kaskadowe (clip-path), na hover zdjęcie unosi się, przybliża i pokazuje podpis, pozostałe przygasają, a nazwa po prawej zmienia się z animacją. Lightbox ma 11 zdjęć ze strzałkami, klawiaturą i swipe.
- Sklep: katalog w `data/products.json`. Płatność online przez Stripe Checkout (BLIK, karta, Przelewy24), funkcja `netlify/functions/create-checkout.mjs`, strona `sukces.html`. Pozycje „od” (kompozycje, wieńce) wyłączają płatność online. Dostawa to stała opłata `delivery_fee` (20 zł, robocza). Bez klucza Stripe sklep przełącza się na płatność przy odbiorze.
- Menu: „Sklep” zamiast „Zamów online”.

## Zmiany v4.1: zamówienie połączone ze sklepem
- Sekcja „Zamów bukiet”: 4 bestsellery ze sklepu (z `data/products.json`, kategoria bukiety, według `rec`) i kafel „Cały sklep”. Kliknięcie otwiera kartę produktu w sklepie (`sklep.html#p=id`). Pod spodem panel „Nie wiesz, co wybrać?”: szybkie zamówienie u florystki w jednym wierszu (wielkość, termin, odbiór, telefon).
- Wejścia do sklepu: przycisk hero „Zamów bukiet”, przycisk w navbarze (z licznikiem koszyka), w lightboxie galerii „Zamów podobny” albo „Zobacz w sklepie”, dolny pasek na mobile (Zadzwoń / Sklep).
- Sklep obsługuje deep link `#p=id` i od razu otwiera kartę produktu.

## Zmiany v4.2: rozwijane menu (mega menu)
- Pozycje w navbarze (Galeria, Sklep, Śluby i dekoracje, Opinie, Kontakt) po najechaniu lub fokusie rozwijają panel z opisem, miniaturami i skrótami. Jeden wspólny panel płynnie zmienia rozmiar i pozycję między pozycjami, treść wjeżdża z kierunku ruchu, elementy pojawiają się kaskadą, a strzałka wskazuje aktywny link. Esc zamyka panel.
- Sklep w menu: kategorie z miniaturami (linki `sklep.html#kat=…`) i bestseller ze zdjęciem.
- Na mobile (burger) pod każdą pozycją jest krótki opis.
- Generator: `tools/mega.py` wstawia panel do `index.html` i `sklep.html`. Treść paneli edytuje się w tym pliku.

## Zmiany v5: spójność
- Kolejność sekcji: Hero, Zamów bukiet, Śluby i dekoracje, Galeria, Opinie, Kontakt, stopka. Każda sekcja ma inną rolę i inny rytm.
- Zamów bukiet: jeden duży polecany bukiet (`featured` w `products.json`) i lista 3 bukietów z miniaturą, opisem i ceną, a pod nią link „Zobacz cały sklep”. Progi u florystki (Mały, Średni, Duży) są liczone z tego samego cennika: najtańszy bukiet plus dopłata za wielkość.
- Galeria pokazuje realizacje (dekoracje, wieńce, nagrobki, detal), a nie produkty ze sklepu. 6 zdjęć, na ostatnim znacznik „+5”, w lightboxie 11 zdjęć.
- Menu: kropka pod pozycją oznacza miejsce, w którym jesteś (strona albo sekcja). Pigułka podąża tylko za kursorem i znika po jego zjechaniu, a przy otwartym panelu zostaje na tej pozycji.
- Wspólny nagłówek (telefon, przycisk lub koszyk, burger poniżej 1140 px) i wspólna stopka na wszystkich stronach. Generatory: `tools/mega.py`, potem `tools/layout.py`.
- Usunięto wstążkę i tryb ciemny.
- Strony `regulamin.html` i `polityka-prywatnosci.html` to projekty z polami TODO, do weryfikacji przez prawnika. W koszyku jest wymagana zgoda na regulamin, a przy formularzu florystki informacja o polityce prywatności.
- SEO: znaczniki Open Graph i `robots.txt` (sitemap po podpięciu domeny).

## Zmiany v5.1: mniejsza skala
- Bazowa wielkość tekstu to 15 px (wcześniej 16). Kontener ma maks. 1120 px. Nagłówki, napis „Galeria”, numer telefonu, cytaty i przyciski są mniejsze o 12–20%. Wartości są w `tools/layout.py`, w sekcji „skala”: jedna zmiana działa na wszystkie strony.

## Zmiany v5.1: nowe zdjęcia (Google Flow)
- Hero: wygenerowany bukiet na kremowym tle (`img/hero.webp` 1376×768, tło podciągnięte do #FBF7F4; mobile `img/hero-m.webp` 768×1376 przez `<picture>`). Panel zdjęcia ma 66% szerokości, wygaszenie z lewej i u dołu.
- Dawne zdjęcie hero (prawdziwy bukiet) to teraz `img/p09.webp`: produkt „Bukiet Pastelowy” i miniatury w menu.
- Śluby: `slub-wiazanka.webp` i `slub-stol.webp` (wygenerowane), zamiast p01/p04. Mega menu Śluby: wiązanka.
- Opinie: `pracownia.webp` (ręce florystki), pasuje do cytatu o układaniu bukietu.
- Kontakt: `kwiaciarnia.webp` (wnętrze w szałwii) zamiast p12.
- Sklep: nowy produkt „Flowerbox Pudrowy” (189 zł, roboczo), `flowerbox.webp`.
- OG: `img/og.jpg` 1200×630 (flat-lay ze wstążką).
- Zdjęcia wygenerowane mają 1376 px. Przy ponownym generowaniu warto pobrać wersję 2K.
- Galeria i karty produktów zostają przy prawdziwych realizacjach.

## Faza 1: przejście na AM Flowers (2026-11-23)
- Strona zostaje klasyczna: bez sklepu i bez kwiatomatu. Sklep, regulamin sklepu i płatności są w AM Flowers (`amflowers.pl`).
- Nagłówek: pod nazwą mały podpis „AM Flowers” ze złotym monogramem.
- Hero: suwak przejścia (złoty uchwyt z monogramem). Przeciągnięcie za 60%, klik albo Enter uruchamia kurtynę: złota linia, szmaragd z wideo jedwabiu, narożniki z wizytówki, hasło „Dwa pokolenia, AMiłość do kwiatów ta sama.”, potem AM Flowers.
- Każdy link do AM Flowers (`data-am-go`) używa tej samej kurtyny.
- Stopka: „Kwiaciarnia Małgorzata rośnie: poznaj AM Flowers”, © Kwiaciarnia Małgorzata · AM Flowers.
- Szczegóły marki: repo `AM_flowers`, folder `brand/`.
