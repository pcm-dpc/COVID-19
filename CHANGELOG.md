# Changelog

Tutte le modifiche al progetto, nuove funzionalità e informazioni sono documentate in questo file

## 2020-03-08

- Modifica: "dati-andamento-nazionale" riportando i totali dei dati delle Regioni
- Rimossa: directory "shape-aree-contenimento" e creata "aree" con "shp" e "geojson"

## 2020-03-10

- Aggiornate le Aree secondo il nuovo DPCM 9 Marzo 2020

## 2020-03-11

- Modifica: "Bolzano" e "Trento" rinominati in "P.A. Bolzano" e "P.A. Trento" in "dati-regioni e "dati-province" ("denominazione_regione")
- Modifica: Friuli V. G. rinominata in "dati-regioni e "dati-province" ("denominazione_regione") in "Friuli Venezia Giulia"

## 2020-03-12

- Aggiunto: Codice di Condotta in italiano (CODE_OF_CONDUCT.md) e in inglese (CODE_OF_CONDUCT_EN.md)
- Aggiunto: Changelog in italiano (CHANGELOG.md) e in inglese (CHANGELOG_EN.md)
- Aggiornate le Aree secondo il nuovo DPCM 11 Marzo 2020

## 2020-03-19

- Aggiunti ultimi dati (latest) csv, nelle rispettive directory, per andamento nazionale (dpc-covid19-ita-andamento-nazionale-latest.csv), regioni (dpc-covid19-ita-regioni-latest.csv) e province (dpc-covid19-ita-province-latest.csv)
- Aggiunti ultimi dati (latest) json, nella directory dati-json, per andamento nazionale (dpc-covid19-ita-andamento-nazionale-latest.json), regioni (dpc-covid19-ita-regioni-latest.json) e province (dpc-covid19-ita-province-latest.json)

## 2020-03-25

- Data nel formato ISO8601 UTC
- Aggiunta: "Note" in "dati-regioni", "dati-province" e "dati-andamento-nazionale"
- Aggiunta: dataset "note"

## 2020-03-30

- Modifica: "totale_attualmente_positivi" rinominato in "totale_positivi" (ricoverati_con_sintomi + terapia_intensiva + isolamento domiciliare) in "dati_regioni" e "dati_andamento_nazionale"
- Modifica: "nuovi_attualmente_positivi" rinominato in "variazione_totale_positivi" (totale_attualmente positivi giorno corrente - totale_attualmente positivi giorno precedente) in "dati_regioni" e "dati_andamento_nazionale"
- Aggiunta: "nuovi_positivi" (totale_casi giorno corrente - totale_casi giorno precedente) in "dati_regioni" e "dati_andamento_nazionale"
- Modifica: Regione "Emilia Romagna" rinominato in "Emilia-Romagna" in "dati-regioni" e "dati-province" ("denominazione_regione")

## 2020-04-20

- Aggiunta: "casi_testati", totale dei soggetti sottoposti al test dal 19/04/2020

## 2020-04-21

- Aggiunta: nuovo shape file con misure di contenimento a livello subregionale (province, comuni e frazioni) con rlativi metadata.

## 2020-04-22

- Aggiunta: nuovo dataset contratti dpc forniture (contratti e pagamenti) in formato csv e json.  [link alla dashboard](https://app.powerbi.com/view?r=eyJrIjoiNzA1YmQ0NDctYzY3ZC00ZTlkLWI1MTQtMThmNTEwNWY3NjM4IiwidCI6IjlhMDZhOTA3LTA2OTUtNDA0YS05NmY4LTRhMWU5YTJmYjQxZCIsImMiOjl9) - [link al dataset ](https://github.com/pcm-dpc/COVID-19/tree/master/dati-contratti-dpc-forniture)

## 2020-04-23

- Aggiunta: metadati del nuovo dataset contratti dpc forniture (contratti e pagamenti) in formato DCAT-AP-IT
- Integrato README con specifiche per il data model dei dataset aree (nazionali e subregionali)

## 2020-04-27

- Aggiunta: aggiornamento al 26/4/2020 shape file e relativi metadata con misure di contenimento a livello subregionale (province, comuni e frazioni).

## 2020-05-04

- Aggiunta: aggiornamento al 4/5/2020 shape file e relativi metadati con misure di contenimento a livello nazionale a seguito del DPCM 26/4/2020.

## 2020-05-06

- Aggiunta: aggiornamento al 03/05/2020 shape file e relativi metadata con misure di contenimento a livello subregionale (province, comuni e frazioni).

## 2020-05-16

- Cambio codice_regione P.A. Bolzano e P.A. Trento: da 04 a 21 per P.A. Bolzano e da 04 a 22 per P.A. Trento (codice provincia)

## 2020-05-18

- Aggiunta: aggiornamento al 18/5/2020 shape file e relativi metadati con misure di contenimento a livello nazionale a seguito del DPCM 17/5/2020.

## Prossimi aggiornamenti

- API Rest (Json) public beta
- GraphQL public beta