<img src="http://opendatadpc.maps.arcgis.com/sharing/rest/content/items/5c8ef7516b5b4bb19f61037b4cd69015/data" alt="COVID-19" data-canonical-src="http://opendatadpc.maps.arcgis.com/sharing/rest/content/items/5c8ef7516b5b4bb19f61037b4cd69015/data" width="400" />

# Dati COVID-19 Italia

[![GitHub license](https://img.shields.io/badge/License-Creative%20Commons%20Attribution%204.0%20International-blue)](https://github.com/pcm-dpc/COVID-19/blob/master/LICENSE)
[![GitHub commit](https://img.shields.io/github/last-commit/pcm-dpc/COVID-19)](https://github.com/pcm-dpc/COVID-19/commits/master)
 

[Sito del Dipartimento della Protezione Civile - Emergenza Coronavirus: la risposta nazionale](http://www.protezionecivile.it/attivita-rischi/rischio-sanitario/emergenze/coronavirus)


Il 31 gennaio 2020, il Consiglio dei Ministri dichiara lo stato di emergenza, per la durata di sei mesi, in conseguenza del rischio sanitario connesso all'infezione da Coronavirus.

Al Capo del Dipartimento della Protezione Civile, Angelo Borrelli, è affidato il coordinamento degli interventi necessari a fronteggiare l'emergenza sul territorio nazionale.  
  
Le principali azioni coordinate dal Capo del Dipartimento sono volte al soccorso e all'assistenza della popolazione eventualmente interessata dal contagio, al potenziamento dei controlli nelle aree aeroportuali e portuali, in continuità con le misure urgenti già adottate dal Ministero della salute, al rientro in Italia dei cittadini che si trovano nei Paesi a rischio e al rimpatrio dei cittadini stranieri nei Paesi di origine esposti al rischio.

Per informare i cittadini e mettere a disposizione i dati raccolti, utili ai soli fini comunicativi e di informazione, il Dipartimento della Protezione Civile ha elaborato un cruscotto geografico interattivo raggiungibile agli indirizzi  [http://arcg.is/C1unv](http://arcg.is/C1unv) (versione desktop) e [http://arcg.is/081a51](http://arcg.is/081a51) (versione mobile) e mette a disposizione, con licenza CC-BY-4.0, le seguenti informazioni aggiornate quotidianamente alle 18:30 (successivamente la conferenza stampa del Capo Dipartimento):

- Dati Andamento nazionale
- Dati json
- Dati regioni
- Dati province
- Schede riepilogative
- Aree
- Note
- Dati contratti DPC forniture

## Avvisi

[Avvisi sui dati andamento COVID-19 Italia](avvisi.md)<br>

## Struttura del repository
```
COVID-19/
│
├── aree/
│   ├── geojson
│   │   ├── dpc-covid-19-ita-aree-comuni.geojson
│   │   ├── dpc-covid19-ita-aree.geojson
│   ├── shp
│   │   ├── dpc-covid19-ita-aree-comuni.dbf
│   │   ├── dpc-covid19-ita-aree-comuni.prj
│   │   ├── dpc-covid19-ita-aree-comuni.shp
│   │   ├── dpc-covid19-ita-aree-comuni.shx
│   │   ├── dpc-covid19-ita-aree.dbf
│   │   ├── dpc-covid19-ita-aree.prj
│   │   ├── dpc-covid19-ita-aree.shp
│   │   ├── dpc-covid19-ita-aree.shx
├── dati-andamento-nazionale/
│   ├── dpc-covid19-ita-andamento-nazionale-*.csv
│   ├── dpc-covid19-ita-andamento-nazionale-latest.csv
│   ├── dpc-covid19-ita-andamento-nazionale.csv
├── dati-contratti-dpc-forniture/
│   ├── dpc-covid19-dati-contratti-dpc-forniture.csv
│   ├── dpc-covid19-dati-pagamenti-contratti-dpc-forniture.csv
│   ├── dati-json
│   │   ├── dpc-covid19-dati-contratti-dpc-forniture.csv
│   │   ├── dpc-covid19-dati-pagamenti-contratti-dpc-forniture.csv
│   ├── file-atti-negoziali
│   │   ├── dpc-contratto-covid19-*.pdf
├── dati-json/
│   ├── dpc-covid19-ita-andamento-nazionale-latest.json
│   ├── dpc-covid19-ita-andamento-nazionale.json
│   ├── dpc-covid19-ita-note-en.json
│   ├── dpc-covid19-ita-note-it.json
│   ├── dpc-covid19-ita-province-latest.json
│   ├── dpc-covid19-ita-province.json
│   ├── dpc-covid19-ita-regioni-latest.json
│   ├── dpc-covid19-ita-regioni.json
├── dati-province/
│   ├── dpc-covid19-ita-province-*.csv
│   ├── dpc-covid19-ita-province-latest.csv
│   ├── dpc-covid19-ita-province.csv
├── dati-regioni/
│   ├── dpc-covid19-ita-regioni-*.csv
│   ├── dpc-covid19-ita-regioni-latest.csv
│   ├── dpc-covid19-ita-regioni.csv
├── note/
│   ├── dpc-covid19-ita-note-en.csv
│   ├── dpc-covid19-ita-note-it.csv
├── schede-riepilogative/
│   ├── province
│   │   ├── dpc-covid19-ita-scheda-province-*.pdf
│   ├── regioni
│   │   ├── dpc-covid19-ita-scheda-regioni-*.pdf
```

## Aggiornamento dei dati

- Dati andamento COVID-19 Italia: ogni giorno alle 18:00<br>
- Dati contratti DPC COVID-19 di fornitura: continua (ogni volta che vengono effettuate operazioni sui contratti)

## Formato dei dati

- [Dati andamento COVID-19 Italia](dati-andamento-covid19-italia.md)<br>
- [Dati contratti DPC COVID-19 di fornitura](dati-contratti-dpc-covid19-fornitura.md)
- [Dati aree misure restrittive COVID19](dati_aree-nazionali-subregionali-misure-restrittive-covid19.md)

## Licenza

[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/deed.it) - [Visualizza licenza](https://github.com/pcm-dpc/COVID-19/blob/master/LICENSE)
