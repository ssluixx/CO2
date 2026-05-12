# CO2 Līmeņa Uzraudzības Sistēma

## Programmas apraksts

Šī programma ir izveidota, lai analizētu un attēlotu CO2 līmeni dažādās dienās, izmantojot datus no CSV faila.

Programma ļauj:

- apskatīt CO2 līmeni konkrētā dienā;
- noteikt, vai CO2 līmenis ir normāls, paaugstināts vai bīstams;
- attēlot visus datus grafikā;
- analizēt gaisa kvalitāti pēc ievadītajiem datiem.

Programma izmanto Flask tīmekļa serveri un Matplotlib grafiku attēlošanai.

---

# Programmas uzstādīšana

Nepieciešams instalēt Python bibliotēkas.

Instalēšana terminālī:

```bash
pip install flask, matplotlib


Pārliecinieties, ka projekta mapē atrodas:

app.py
CO2.csv
templates/


Projekta struktūra:

project/
│
├── app.py
├── CO2.csv
└── templates/
    ├── index.html
    ├── day.html
    └── chart.html

Failu nozīme:

app.py — galvenais programmas fails
CO2.csv — CO2 datu fails
index.html — sākumlapa
day.html — konkrētas dienas apskate
chart.html — grafika attēlošana


Programmas palaišana
Terminālī ievadīt:

python app.py

Pēc palaišanas atvērt pārlūkā:
http://127.0.0.1:5000/


Programmas izmantošana:
CO2 līmeņa apskate konkrētā dienā

1) Atvērt sākumlapu
2) Izvēlēties Pārbaudīt konkrētu dienu
3) Ievadīt dienas numuru
4) Spiest pogu

Programma parādīs:

CO2 vērtību ppm statusu:
1) Normāls līmenis
2) Paaugstināts līmenis
3) Bīstami augsts līmenis

Grafika apskate

Atvērt sākumlapu
Izvēlēties Apskatīt pilnu grafiku
Programma attēlos visu CO2 līmeņu grafiku.

Sagaidāmā izvade
Programma parāda:

CO2 skaitlisko vērtību
gaisa kvalitātes statusu
vizuālu grafiku pa dienām

Iespējamie statusi:

normal — drošs līmenis
medium — paaugstināts līmenis
high — bīstams līmenis

Piemēri

Piemērs 1

Ievade:

283

Izvade:

CO2: 2000.89 ppm
Bīstami augsts līmenis

Piemērs 2

Ievade:

150

Izvade:

CO2: 369.41 ppm
Normāls līmenis

Piemērs 3
Grafika apskate

Programma attēlo līkni ar visiem CO2 datiem, lai analizētu izmaiņas laika gaitā.


Iespējamie uzlabojumi

Nākotnē programmai var pievienot:
1)datu pievienošanu no tīmekļa formas;
2)automātiskus brīdinājumus;
3)statistikas aprēķinus;
4)datu filtrēšanu pēc periodiem;
5)vairāku kabinetu analīzi.
