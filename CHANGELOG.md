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

## Prossimi aggiornamenti

- API Rest (Json)
- GraphQL

## Ipotesi modifiche

- Rendere in lingua inglese i dataset e nomi dei campi
- Cambio codice_regione P.A. Bolzano e P.A. Trento: da 04 a 21 per P.A. Bolzano e da 04 a 22 per P.A. Trento (codice provincia)