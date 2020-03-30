# Changelog

All changes to the project, new features and information are documented in this file

## 2020-03-08

- Change: dataset "dati-andamento-nazionale" by reporting the total data of the Regions
- Removed: directory "shape-aree-contenimento" with "shp" and "geojson"

## 2020-03-10

- Areas updated according to the new Decree of the President of the Council of Ministers (DPCM) March 09, 2020

## 2020-03-11

- Change: "Bolzano" and "Trento" renamed to "P.A. Bolzano" and "P.A. Trento" in "dati-regioni and "dati-province" ("denominazione_regione")
- Change: "Friuli V.G." renamed to "Friuli Venezia Giulia" in "dati-regioni and "dati-province" ("denominazione_regione") to "Friuli Venezia Giulia"

## 2020-03-12

- Add: code of conduct in italian language (CODE_OF_CONDUCT.md) and in english language (CODE_OF_CONDUCT_EN.md)
- Add: changelog in italian language (CHANGELOG.md) and in english language (CHANGELOG_EN.md)
- Areas updated according to the new Decree of the President of the Council of Ministers (DPCM) March 11, 2020

## 2020-03-19

- Added latest data (latest) csv, into their respective directory, per national trend (dpc-covid19-ita-andamento-nazionale-latest.csv), regions (dpc-covid19-ita-regioni-latest.csv) and provinces (dpc-covid19-ita-province-latest.csv)
- Added latest data (latest) json, in data-json directory, for national trend (dpc-covid19-ita-andamento-nazionale-latest.json), regions (dpc-covid19-ita-regioni-latest.json) and provinces ( dpc-covid19-ita-province-latest.json)

## 2020-03-25

- Date in ISO8601 format UTC
- Add: "Note" (Notes) in "dati-regioni", "dati-province" and "dati-andamento-nazionale"
- Add: "note" dataset

## Next updates - 2020-03-31 @ 12:00 (italian hour)

- Change: "totale_attualmente_positivi" renamed to "totale_positivi" in  (ricoverati_con_sintomi + terapia_intensiva + totale_ospedalizzati) in "dati_regioni" and "dati_andamento_nazionale"
- Add: "variazione_totale_positivi" (totale_attualmente positivi current day - totale_attualmente positivi previous day) in "dati_regioni" and "dati_andamento_nazionale"
- Change: "nuovi_attualmente_positivi" renamed to "nuovi_positivi" (totale_casi current day - totale_casi previous day) in "dati_regioni" and "dati_andamento_nazionale"
- Change: Regione "Emilia Romagna" renamed to "Emilia-Romagna" in "dati-regioni" and "dati-province" ("denominazione_regione")
