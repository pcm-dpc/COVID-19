<img src="http://opendatadpc.maps.arcgis.com/sharing/rest/content/items/5c8ef7516b5b4bb19f61037b4cd69015/data" alt="COVID-19" data-canonical-src="http://opendatadpc.maps.arcgis.com/sharing/rest/content/items/5c8ef7516b5b4bb19f61037b4cd69015/data" width="400" />

# Dati COVID-19 Italia

[![GitHub license](https://img.shields.io/badge/License-Creative%20Commons%20Attribution%204.0%20International-blue)](https://github.com/pcm-dpc/COVID-19/blob/master/LICENSE)
[![GitHub commit](https://img.shields.io/github/last-commit/pcm-dpc/COVID-19)](https://github.com/pcm-dpc/COVID-19/commits/master)

## Aggiornamento effettuato!

## Aggiornamenti schema dataset 30/03/2020 @ 12:00 (Ora italiana)
## Dataset schema update 30/03/2020 @ 12:00 (Italian hour)

### Dataset:
- dati_regioni (csv / json)
- dati_andamento_nazionale (csv / json)
- dati_province (csv / json) - (solo modifica nome/only change name "Emilia-Romagna" in "Emilia-Romagna")

### IT
- Modifica: "totale_attualmente_positivi" rinominato in "totale_positivi" (ricoverati_con_sintomi + terapia_intensiva + isolamento domiciliare) in "dati_regioni" e "dati_andamento_nazionale"
- Modifica: "nuovi_attualmente_positivi" rinominato in "variazione_totale_positivi" (totale_attualmente positivi giorno corrente - totale_attualmente positivi giorno precedente) in "dati_regioni" e "dati_andamento_nazionale"
- Aggiunta: "nuovi_positivi" (totale_casi giorno corrente - totale_casi giorno precedente) in "dati_regioni" e "dati_andamento_nazionale"
- Modifica: Regione "Emilia Romagna" rinominato in "Emilia-Romagna" in "dati-regioni" e "dati-province" ("denominazione_regione")

### EN
- Change: "totale_attualmente_positivi" renamed to "totale_positivi" (ricoverati_con_sintomi + terapia_intensiva + isolamento domiciliare) in "dati_regioni" and "dati_andamento_nazionale"
- Change: "nuovi_attualmente_positivi" renamed to "variazione_totale_positivi" (totale_attualmente positivi giorno corrente - totale_attualmente positivi giorno precedente) in "dati_regioni" and "dati_andamento_nazionale"
- Add: "nuovi_positivi" (totale_casi giorno corrente - totale_casi giorno precedente) in "dati_regioni" and "dati_andamento_nazionale"
- Change: Regione "Emilia Romagna" renamed to "Emilia-Romagna" in "dati-regioni" and "dati-province" ("denominazione_regione")

### Esempi / Examples

* dati_regioni (esempio csv)
```
data,stato,ricoverati_con_sintomi,terapia_intensiva,totale_ospedalizzati,isolamento_domiciliare,totale_positivi,variazione_totale_positivi,nuovi_positivi,dimessi_guariti,deceduti,totale_casi,tamponi,note_it,note_en
2020-03-30T17:00:00,ITA,27795,3981,31776,43752,75528,1648,4050,14620,11591,101739,477359,,
```

* dati_andamento_nazionale (esempio csv)
```
data,stato,codice_regione,denominazione_regione,lat,long,ricoverati_con_sintomi,terapia_intensiva,totale_ospedalizzati,isolamento_domiciliare,totale_positivi,variazione_totale_positivi,nuovi_positivi,dimessi_guariti,deceduti,totale_casi,tamponi,note_it,note_en
2020-03-30T17:00:00,ITA,03,Lombardia,45.46679409,9.190347404,11815,1330,13145,11861,25006,-386,1154,10337,6818,42161,111057,,
```

## Stiamo lavorando per fornire nuovi dataset, dashboard e al perfezionamento di quelli esistenti.
## We are working to provide new datasets, dashboard and on the refinement of existing ones.

## README e Wiki in aggiornamento
## README and Wiki under update

## Avvisi

```diff
- 29/03/2020: dati Regione Emilia-Romagna parziali (dato tampone non aggiornato).
- 26/03/2020: dati Regione Piemonte parziali (-50 deceduti - comunicazione tardiva).
- 18/03/2020: dati Regione Campania non pervenuti.
- 18/03/2020: dati Provincia di Parma non pervenuti.
- 17/03/2020: dati Provincia di Rimini non aggiornati.
- 16/03/2020: dati P.A. Trento e Puglia non pervenuti.
- 11/03/2020: dati Regione Abruzzo non pervenuti.
- 10/03/2020: dati Regione Lombardia parziali.
- 07/03/2020: dati Brescia +300 esiti positivi
```
 

[Sito del Dipartimento della Protezione Civile - Emergenza Coronavirus: la risposta nazionale](http://www.protezionecivile.it/attivita-rischi/rischio-sanitario/emergenze/coronavirus)


Il 31 gennaio 2020, il Consiglio dei Ministri dichiara lo stato di emergenza, per la durata di sei mesi, in conseguenza del rischio sanitario connesso all'infezione da Coronavirus.

Al Capo del Dipartimento della Protezione Civile, Angelo Borrelli, è affidato il coordinamento degli interventi necessari a fronteggiare l'emergenza sul territorio nazionale.  
  
Le principali azioni coordinate dal Capo del Dipartimento sono volte al soccorso e all'assistenza della popolazione eventualmente interessata dal contagio, al potenziamento dei controlli nelle aree aeroportuali e portuali, in continuità con le misure urgenti già adottate dal Ministero della salute, al rientro in Italia dei cittadini che si trovano nei Paesi a rischio e al rimpatrio dei cittadini stranieri nei Paesi di origine esposti al rischio.

Per informare i cittadini e mettere a disposizione i dati raccolti, utili ai soli fini comunicativi e di informazione, il Dipartimento della Protezione Civile ha elaborato un cruscotto geografico interattivo raggiungibile agli indirizzi  [http://arcg.is/C1unv](http://arcg.is/C1unv) (versione desktop) e [http://arcg.is/081a51](http://arcg.is/081a51) (versione mobile) e mette a disposizione, con licenza CC-BY-4.0, le seguenti informazioni aggiornate quotidianamente alle 18:30 (successivamente la conferenza stampa del Capo Dipartimento):

- Andamento nazionale
- Dati json
- Dati province
- Dati regioni
- Schede riepilogative
- Aree

## Struttura del repository
```
COVID-19/
│
├── andamento-nazionale/
│   ├── dpc-covid19-ita-andamento-nazionale-yyyymmdd.csv
├── aree/
│   ├── geojson
│   │   ├── dpc-covid19-ita-aree.geojson
│   ├── shp
│   │   ├── dpc-covid19-ita-aree.shp
├── dati-province/
│   ├── dpc-covid19-ita-province-yyyymmdd.csv
├── dati-json/
│   ├── dpc-covid19-ita-*.json
├── dati-regioni/
│   ├── dpc-covid19-ita-regioni-yyyymmdd.csv
├── schede-riepilogative/
│   ├── province
│   │   ├── dpc-covid19-ita-scheda-province-yyyymmdd.pdf
│   ├── regioni
│   │   ├── dpc-covid19-ita-scheda-regioni-yyyymmdd.pdf
```


## Formato dei dati

### Dati per Regione

**Directory:**  dati-regioni<br>
**Struttura file giornaliero:** dpc-covid19-ita-regioni-yyyymmdd.csv (dpc-covid19-ita-regioni-20200224.csv)<br>
**File complessivo:** dpc-covid19-ita-regioni.csv<br>
**File ultimi dati (latest):** dpc-covid19-ita-regioni-latest.csv

| Nome campo                  | Descrizione                       | Description                            | Formato                       | Esempio             |
|-----------------------------|-----------------------------------|----------------------------------------|-------------------------------|---------------------|
| **data**                        | Data dell’informazione            | Date of notification                   | YYYY-MM-DD HH:MM:SS (ISO 8601) Ora italiana | 2020-03-05 12:15:45 |
| **stato**                       | Stato di riferimento              | Country of reference                   | XYZ (ISO 3166-1 alpha-3)      | ITA                 |
| **codice_regione**              | Codice della Regione (ISTAT 2019) | Code of the Region (ISTAT 2019)        | Numero                        | 13                  |
| **denominazione_regione**       | Denominazione della Regione       | Name of the Region                     | Testo                         | Abruzzo             |
| **lat**                         | Latitudine                        | Latitude                               | WGS84                         | 42.6589177          |
| **long**                        | Longitudine                       | Longitude                              | WGS84                         | 13.70439971         |
| **ricoverati_con_sintomi**      | Ricoverati con sintomi            | Hospitalised patients with symptoms    | Numero                        | 3                   |
| **terapia_intensiva**           | Ricoverati in terapia intensiva   | Intensive Care                         | Numero                        | 3                   |
| **totale_ospedalizzati**        | Totale ospedalizzati              | Total hospitalised patients            | Numero                        | 3                   |
| **isolamento_domiciliare**      | Persone in isolamento domiciliare | Home confinement                       | Numero                        | 3                   |
| **totale_positivi** | Totale attualmente positivi (ospedalizzati + isolamento domiciliare)      | Total amount of current positive cases (Hospitalised patients + Home confinement)  | Numero                        | 3                   |
| **variazione_totale_positivi**  | Variazione del totale positivi (totale_positivi giorno corrente - totale_positivi giorno precedente)       | New amount of current positive cases (totale_positivi current day - totale_positivi previous day)  | Numero                        | 3                   |
| **nuovi_positivi**  | Nuovi attualmente positivi (totale_casi giorno corrente - totale_casi giorno precedente)       | New amount of current positive cases (totale_casi current day - totale_casi previous day)  | Numero                        | 3                   |
| **dimessi_guariti**             | Persone dimesse guarite           | Recovered                              | Numero                        | 3                   |
| **deceduti**                    | Persone decedute                  | Deaths                                 | Numero                        | 3                   |
| **totale_casi**                 | Totale casi positivi              | Total amount of positive cases         | Numero                        | 3                   |
| **tamponi**                     | Totale tamponi                    | Tests performed                        | Numero                        | 3                   |
| **note_it**                     | Note in lingua italiana                    | Notes in italian language                        | Test                        | pd-IT-000                   |
| **note_en**                     | Note in lingua inglese                    | Notes in english language                        | Testo                        | pd-EN-000                   |


*Le Province autonome di Trento e Bolzano sono indicate in "denominazione regione" e con il codice 04 del Trentino Alto Adige.*<br>
*Viene messo a disposizione un file JSON complessivo di tutte le date nella cartella "dati-json": dpc-covid19-ita-regioni.json* e rispettivo file ultimi dati (latest) dpc-covid19-ita-regioni-latest.json

### Dati per Provincia

**Directory:**  dati-province<br>
**Struttura file giornaliero:** dpc-covid19-ita-province-yyyymmdd.csv (dpc-covid19-ita-province-20200224.csv)<br>
**File complessivo:** dpc-covid19-ita-province.csv<br>
**File ultimi dati (latest):** dpc-covid19-ita-province-latest.csv

| Nome campo              | Descrizione                         | Description                     | Formato            | Esempio              |
|-------------------------|-------------------------------------|---------------------------------|--------------------|----------------------|
| **data**                    | Data dell’informazione              | Date of notification            | YYYY-MM-DD HH:MM:SS (ISO 8601) Ora italiana           | 2020-03-05 12:15:45 |                   |
| **stato**                   | Stato di riferimento                | Country of reference            | ISO 3166-1 alpha-3 | ITA                  |
| **codice_regione**          | Codice della Regione (ISTAT 2019)   | Code of the Region (ISTAT 2019) | Numero             | 13                   |
| **denominazione_regione**   | Denominazione della Regione         | Name of the Region              | Testo              | Abruzzo              |
| **codice_provincia**        | Codice della Provincia (ISTAT 2019) | Code of the Province            | Numero             | 067                  |
| **denominazione_provincia** | Denominazione della provincia       | Name of the Province            | Testo              | Teramo               |
| **sigla_provincia**         | Sigla della Provincia               | Province abbreviation           | Testo              | TE                   |
| **lat**                     | Latitudine                          | Latitude                        | WGS84              | 42.6589177           |
| **long**                    | Longitudine                         | Longitude                       | WGS84              | 13.70439971          |
| **totale_casi**             | Totale casi positivi                | Total amount of positive cases  | Numero             | 3                    |

*Le Province autonome di Trento e Bolzano sono indicate in "denominazione regione" e con il codice 04 del Trentino Alto Adige.*<br>
*Ogni Regione ha una Provincia denominata "In fase di definizione/aggiornamento" con il codice provincia da 979 a 999, utile ad indicare i dati ancora non assegnati alle Province.*<br>
*Viene messo a disposizione un file JSON complessivo di tutte le date nella cartella "dati-json": dpc-covid19-ita-province.json* e rispettivo file ultimi dati (latest) dpc-covid19-ita-province-latest.json

### Andamento nazionale

**Directory:**  dati-andamento-nazionale<br>
**Struttura file giornaliero:** dpc-covid19-ita-andamento-nazionale-yyyymmdd.csv (dpc-covid19-ita-andamento-nazionale-20200224.csv)<br>
**File complessivo:** dpc-covid19-ita-andamento-nazionale.csv<br>
**File ultimi dati (latest):** dpc-covid19-ita-regioni-latest.csv


| Nome campo                  | Descrizione                       | Description                            | Formato                       | Esempio             |
|-----------------------------|-----------------------------------|----------------------------------------|-------------------------------|---------------------|
| **data**                        | Data dell’informazione            | Date of notification                   | YYYY-MM-DD HH:MM:SS (ISO 8601) Ora italiana | 2020-03-05 12:15:45 |
| **stato**                       | Stato di riferimento              | Country of reference                   | XYZ (ISO 3166-1 alpha-3)      | ITA                 |
| **ricoverati_con_sintomi**      | Ricoverati con sintomi            | Hospitalised patients with symptoms    | Numero                        | 3                   |
| **terapia_intensiva**           | Ricoverati in terapia intensiva   | Intensive Care                         | Numero                        | 3                   |
| **totale_ospedalizzati**        | Totale ospedalizzati              | Total hospitalised patients            | Numero                        | 3                   |
| **isolamento_domiciliare**      | Persone in isolamento domiciliare | Home confinement                       | Numero                        | 3                   |
| **totale_positivi** | Totale attualmente positivi (ospedalizzati + isolamento domiciliare)      | Total amount of current positive cases (Hospitalised patients + Home confinement)  | Numero                        | 3                   |
| **variazione_totale_positivi**  | Variazione del totale positivi (totale_positivi giorno corrente - totale_positivi giorno precedente)       | News amount of current positive cases (totale_positivi current day - totale_positivi previous day)  | Numero                        | 3                   |
| **nuovi_positivi**  | Nuovi attualmente positivi (totale_casi giorno corrente - totale_casi giorno precedente)       | News amount of current positive cases (totale_casi current day - totale_casi previous day)  | Numero                        | 3                   |
| **dimessi_guariti**             | Persone dimesse guarite           | Recovered                              | Numero                        | 3                   |
| **deceduti**                    | Persone decedute                  | Deaths                                 | Numero                        | 3                   |
| **totale_casi**                 | Totale casi positivi              | Total amount of positive cases         | Numero                        | 3                   |
| **tamponi**                     | Totale tamponi                    | Tests performed                        | Numero                        | 3                   |
| **note_it**                     | Note in lingua italiana                    | Notes in italian language                        | Test                        | pd-IT-000                   |
| **note_en**                     | Note in lingua inglese                    | Notes in english language                        | Testo                        | pd-EN-000                   |



*Viene messo a disposizione un file JSON complessivo di tutte le date nella cartella "dati-json": dpc-covid19-ita-andamento-nazionale.json* e rispettivo file ultimi dati (latest) dpc-covid19-ita-andamento-nazionale-latest.json
<br><br>
**Licenza:** [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/deed.en) - [Visualizza licenza](https://github.com/pcm-dpc/COVID-19/blob/master/LICENSE)
<br><br><br>
**Editore/Autore del dataset:** Dipartimento della Protezione Civile<br>
**Temi del dataset:** [Salute umana e sicurezza - Human health and safety](http://inspire.ec.europa.eu/theme/hh) (Inspire)<br>
**Categoria ISO 19115:** Salute<br>
*Dati forniti dal Ministero della Salute*<br>
*Elaborazione e gestione dati a cura del Dipartimento della Protezione Civile*
