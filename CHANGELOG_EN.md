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

## 2020-03-30

- Change: "totale_attualmente_positivi" renamed to "totale_positivi" (ricoverati_con_sintomi + terapia_intensiva + isolamento domiciliare) in "dati_regioni" and "dati_andamento_nazionale"
- Change: "nuovi_attualmente_positivi" renamed to "variazione_totale_positivi" (totale_attualmente positivi giorno corrente - totale_attualmente positivi giorno precedente) in "dati_regioni" and "dati_andamento_nazionale"
- Add: "nuovi_positivi" (totale_casi giorno corrente - totale_casi giorno precedente) in "dati_regioni" and "dati_andamento_nazionale"
- Change: Regione "Emilia Romagna" renamed to "Emilia-Romagna" in "dati-regioni" and "dati-province" ("denominazione_regione")

## 2020-04-20

- Add: "casi_testati", total number of people tested from 2020-04-19

##  2020-04-21

- Add: new shape file with subregional containment measures (provinces, municipalities and hamlets) with related metadata.

## 2020-04-22

- Add: new dataset dpc supplies contracts (contracts and payments) in csv and json format. [link to dashboard](https://app.powerbi.com/view?r=eyJrIjoiNzA1YmQ0NDctYzY3ZC00ZTlkLWI1MTQtMThmNTEwNWY3NjM4IiwidCI6IjlhMDZhOTA3LTA2OTUtNDA0YS05NmY4LTRhMWU5YTJmYjQxZCIsImMiOjl9) - [link to dataset ](https://github.com/pcm-dpc/COVID-19/tree/master/dati-contratti-dpc-forniture)

## 2020-04-22

- Add:metadata of the new dpc supplies contracts dataset (contracts and payments) in DCAT-AP-IT format
- Integrated README with specifications for the data model of the dataset areas (national and subregional)

## Next updated

- API Rest (Json)
- GraphQL

## hypothesis changes

- Change codice_regione for P.A. Bolzano and P.A. Trento: from 04 to 21 for P.A. Bolzano and from 04 to 22 for P.A. Trento (province code)
