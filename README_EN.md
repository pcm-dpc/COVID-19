<img src="http://opendatadpc.maps.arcgis.com/sharing/rest/content/items/5c8ef7516b5b4bb19f61037b4cd69015/data" alt="COVID-19" data-canonical-src="http://opendatadpc.maps.arcgis.com/sharing/rest/content/items/5c8ef7516b5b4bb19f61037b4cd69015/data" width="400" />

# Italy's COVID-19 Data

[![GitHub license](https://img.shields.io/github/license/pcm-dpc/COVID-19)](https://github.com/pcm-dpc/COVID-19/blob/master/license)
[![GitHub commit](https://img.shields.io/github/last-commit/pcm-dpc/COVID-19)](https://img.shields.io/github/last-commit/pcm-dpc/COVID-19)

[Website of the Dipartimento della Protezione Civile - Emergenza Coronavirus: la risposta nazionale](http://www.protezionecivile.it/attivita-rischi/rischio-sanitario/emergenze/coronavirus)


On the 31 January 2020, the Council of Ministers declared a six months state of emergency in response to the health risk associated with the coronavirus infection. The Head of the Civil Protection Department, Angelo Borrelli, was appointed as the coordinator of all the interventions necessary to deal with the emergency.  

The main focus of the department were aimed at the rescue and assistance of the population affected by the infection, the strengthening of controls in airports and port areas, the return to Italy of its citizens who were in areas deemed at risk and the repatriation of foreign citizens to their countries of origin if they were exposed to the infection.

In order to inform the citizens and to make the data collected available, useful ONLY for communication and information purposes, the Civil Protection Department has developed an interactive geographical dashboard that can be reached at the addresses [http://arcg.is/C1unv](http://arcg.is/C1unv) (desktop version) and [http://arcg.is/081a51](http://arcg.is/081a51) (mobile version) and it makes available, under license CC-BY-4.0, the following information updated daily at 6:30 p.m. (30 minutes after the press conference from the head of the department):


- Andamento nazionale (National trend)
- Dati json (Json data)
- Dati province (Provinces data)
- Dati regioni (Regions data)
- Schede riepilogative (Summary sheets)
- Shape aree di contenimento (Shapes of containment areas)

## Structure of the repository
```
COVID-19/
│
├── andamento-nazionale/
│   ├── dpc-covid19-ita-andamento-nazionale-yyyymmdd.csv
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
├── shape-aree-contenimento/
│   ├── covid-19-aree.*
```


## Data format

### Data divided by region

**Directory:** `dati-regioni`

**Path daily file:** `dpc-covid19-ita-regioni-yyyymmdd.csv` (example:`dpc-covid19-ita-regioni-20200224.csv`)

**Recap file:** `dpc-covid19-ita-regioni.csv`

| Name                 | Descrizione (Italian)                      | Description                            | Format                       | Example             |
|-----------------------------|-----------------------------------|----------------------------------------|-------------------------------|---------------------|
| **data**                        | Data dell’informazione            | Date of notification                   | YYYY-MM-DD HH:MM:SS (ISO 8601) Italian time | 2020-03-05 12:15:45 |
| **stato**                       | Stato di riferimento              | Country of reference                   | XYZ (ISO 3166-1 alpha-3)      | ITA                 |
| **codice_regione**              | Codice della Regione (ISTAT 2019) | Code of the Region (ISTAT 2019)        | Number                        | 13                  |
| **denominazione_regione**       | Denominazione della Regione       | Name of the Region                     | String                         | Abruzzo             |
| **lat**                         | Latitudine                        | Latitude                               | WGS84                         | 42.6589177          |
| **long**                        | Longitudine                       | Longitude                              | WGS84                         | 13.70439971         |
| **ricoverati_con_sintomi**      | Ricoverati con sintomi            | Hospitalised patients with symptoms    | Number                        | 3                   |
| **terapia_intensiva**           | Ricoverati in terapia intensiva   | Intensive Care                         | Number                        | 3                   |
| **totale_ospedalizzati**        | Totale ospedalizzati              | Total hospitalised patients            | Number                        | 3                   |
| **isolamento_domiciliare**      | Persone in isolamento domiciliare | Home confinement                       | Number                        | 3                   |
| **totale_attualmente_positivi** | Totale attualmente positivi (ospedalizzati + isolamento domiciliare)      | Total amount of current positive cases (Hospitalised patients + Home confinement)  | Number                        | 3                   |
| **nuovi_attualmente_positivi**  | Nuovi attualmente positivi (ospedalizzati + isolamento domiciliare)       | News amount of current positive cases (Hospitalised patients + Home confinement)  | Number                        | 3                   |
| **dimessi_guariti**             | Persone dimesse guarite           | Recovered                              | Number                        | 3                   |
| **deceduti**                    | Persone decedute                  | Death                                  | Number                        | 3                   |
| **totale_casi**                 | Totale casi positivi              | Total amount of positive cases         | Number                        | 3                   |
| **tamponi**                     | Totale tamponi                    | Tests performed                        | Number                        | 3                   |

*The Autonomous provinces of Trento and Bolzano are listed separately in the "region name" but they both share the code 04 of Trentino Alto Adige as "codice_regione".* 

*A JSON file containing all the information for all the dates is made available at the path: `dati-json/dpc-covid19-ita-regioni.json`* 

### Data divided by province

**Directory:** `dati-province`

**Path daily file:** `dpc-covid19-ita-province-yyyymmdd.csv` (example: `dpc-covid19-ita-province-20200224.csv`)

**Recap file:** `dpc-covid19-ita-province.csv`

| Name              | Descrizione (Italian)                       | Description                     | Format            | Example              |
|-------------------------|-------------------------------------|---------------------------------|--------------------|----------------------|
| **data**                    | Data dell’informazione              | Date of notification            | YYYY-MM-DD HH:MM:SS Italian time (ISO 8601)           | 2020-03-05 12:15:45 |                   |
| **stato**                   | Stato di riferimento                | Country of reference            | ISO 3166-1 alpha-3 | ITA                  |
| **codice_regione**          | Codice della Regione (ISTAT 2019)   | Code of the Region (ISTAT 2019) | Number             | 13                   |
| **denominazione_regione**   | Denominazione della Regione         | Name of the Region              | String              | Abruzzo              |
| **codice_provincia**        | Codice della Provincia (ISTAT 2019) | Code of the Province            | Number             | 067                  |
| **denominazione_provincia** | Denominazione della provincia       | Name of the Province            | String              | Teramo               |
| **sigla_provincia**         | Sigla della Provincia               | Province abbreviation           | String              | TE                   |
| **lat**                     | Latitudine                          | Latitude                        | WGS84              | 42.6589177           |
| **long**                    | Longitudine                         | Longitude                       | WGS84              | 13.70439971          |
| **totale_casi**             | Totale casi positivi                | Total amount of positive cases  | Number             | 3                    |

*The Autonomous provinces of Trento and Bolzano are listed separately in the "region name" but they both share the code 04 of Trentino Alto Adige as "codice_regione".* 

*Each Region has a "fake" province named `In fase di definizione/aggiornamento` (in the definition/updating phase) with province code from 979 to 999. This code is used to indicate that the data was not yet assigned to a specific province.*

*A JSON file containing all the information for all the dates is made available in at the path: `dati-json/dpc-covid19-ita-province.json`*

### National trend

**Directory:** `dati-andamento-nazionale`

**Path daily file:** `dpc-covid19-ita-andamento-nazionale-yyyymmdd.csv` (example: `dpc-covid19-ita-andamento-nazionale-20200224.csv`)

**Recap file:** `dpc-covid19-ita-andamento-nazionale.csv`


| Name               | Descrizione  (Italian)                      | Description                            | Format            | Example              |
|----------------------------|-----------------------------------|----------------------------------------|--------------------|----------------------|
| **data**                       | Data dell’informazione            | Date of notification                   | YYYY-MM-DD HH:MM:SS Italian time (ISO 8601)           | 2020-03-05 12:15:45 |                                  |                                        |                    |                      |
| **stato**                      | Stato di riferimento              | Country of reference                   | ISO 3166-1 alpha-3 | ITA                  |
| **ospedalizzati**              | Totale ospedalizzati              | Total hospitalised patients            | Number             | 3                    |
| **isolamento_domiciliare**     | Persone in isolamento domiciliare | Home confinement                       | Number             | 3                    |
| **attualmente_positivi**       | Totale attualmente positivi       | Total amount of current positive cases | Number             | 3                    |
| **dimessi_guariti**            | Persone dimesse guarite           | Recovered                              | Number             | 3                    |
| **deceduti**                   | Persone decedute                  | Death                                  | Number             | 3                    |
| **totale_casi**                | Totale casi positivi              | Total amount of positive cases         | Number             | 3                    |
| **nuovi_attualmente_positivi** | Nuovi attualmente positivi        | News amount of current positive cases  | Number             | 3                    |

*A JSON file containing all the information for all the dates is made available at the path: `dati-json/dpc-covid19-ita-andamento-nazionale.json`*

**Licence:** [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/deed.en) - [Go to licence](https://github.com/pcm-dpc/COVID-19/blob/master/LICENSE)


**Creator of the dataset:** Dipartimento della Protezione Civile

**Theme of the dataset:** [Salute umana e sicurezza - Human health and safety](http://inspire.ec.europa.eu/theme/hh) (Inspire)

**ISO 19115 Category:** Salute/Health

*Dati forniti dal Ministero della Salute*

*Elaborazione e gestione dati a cura del Dipartimento della Protezione Civile*