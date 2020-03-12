<img src="http://opendatadpc.maps.arcgis.com/sharing/rest/content/items/5c8ef7516b5b4bb19f61037b4cd69015/data" alt="COVID-19" data-canonical-src="http://opendatadpc.maps.arcgis.com/sharing/rest/content/items/5c8ef7516b5b4bb19f61037b4cd69015/data" width="400" />

# Italian COVID-19 Data 

[![GitHub license](https://img.shields.io/badge/License-Creative%20Commons%20Attribution%204.0%20International-blue)](https://github.com/pcm-dpc/COVID-19/blob/master/LICENSE)
[![GitHub commit](https://img.shields.io/github/last-commit/pcm-dpc/COVID-19)](https://github.com/pcm-dpc/COVID-19/commits/master)

## Announcements

```diff
- 10/03/2020: partial data for Regione Lombardia.
- 11/03/2020: data from Regione Abruzzo not received.
```
 

[Department of Italian Civil Protection website - Coronavirus emergency: the national response](http://www.protezionecivile.it/attivita-rischi/rischio-sanitario/emergenze/coronavirus) (in Italian)

On January 31, 2020, the Italian Council of Ministers declared a state of emergency for six months as a consequence of the health risk associated with Coronavirus infection.

The Head of the Department of Civil Protection, Angelo Borrelli, is responsible for coordinating the interventions necessary to face the emergency on the national territory.

The main actions, coordinated by the Head of the Department, are aimed to rescuing and assisting the population possibly affected by the infection, the strengthening of controls in airport and port areas, in continuity with the urgent measures already adopted by the Ministry of Health, on returning to Italy of citizens who are in countries at risk and the repatriation of foreign citizens to countries of origin exposed to risk.

To inform citizens and make the collected data available, useful for communication and information purposes only, the Italian Department of Civil Protection has developed an interactive geographic dashboard that can be reached at the addresses  [http://arcg.is/C1unv](http://arcg.is/C1unv) (desktop version) and [http://arcg.is/081a51](http://arcg.is/081a51) (mobile version). In addition, the following information, updated daily at 18:30 (after the Head of Department press conference), are available with CC-BY-4.0 license:

- National trend (andamento nazionale)
- Json data      (dati json)
- Data by Province (dati province)
- Data by region (dati regioni)
- Summary sheets (schede riepilogative)
- Geographical areas (aree)

## Repository structure
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


## Data Format

### Regional Data

**Directory:**  dati-regioni

**Structure of the daily file:** dpc-covid19-ita-regioni-yyyymmdd.csv (dpc-covid19-ita-regioni-20200224.csv)

**Overall data file:** dpc-covid19-ita-regioni.csv

| Field Name                  | Description (Italian)             | Description                            | Format                        | Example             |
|-----------------------------|-----------------------------------|----------------------------------------|-------------------------------|---------------------|
| **data**                        | Data dell’informazione            | Date of notification                   | YYYY-MM-DD HH:MM:SS (ISO 8601) Ora italiana | 2020-03-05 12:15:45 |
| **stato**                       | Stato di riferimento              | Country of reference                   | XYZ (ISO 3166-1 alpha-3)      | ITA                 |
| **codice_regione**              | Codice della Regione (ISTAT 2019) | Code of the Region (ISTAT 2019)        | Number                        | 13                  |
| **denominazione_regione**       | Denominazione della Regione       | Name of the Region                     | Text string                         | Abruzzo             |
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


*The autonomous provinces of Trento and Bolzano are indicated in "region designation" and with the Trentino Alto Adige code 04.*

*An overall JSON file of all dates is available in the "data-json" folder: dpc-covid19-eng-regions.json*

### Data by Province

**Directory:**  dati-province

**Structure of the daily file:** dpc-covid19-ita-province-yyyymmdd.csv (dpc-covid19-ita-province-20200224.csv)

**Overall data file:** dpc-covid19-ita-province.csv

| Field Name              | Description (Italian)               | Description                     | Format             | Example              |
|-------------------------|-------------------------------------|---------------------------------|--------------------|----------------------|
| **data**                    | Data dell’informazione              | Date of notification            | YYYY-MM-DD HH:MM:SS (ISO 8601) Ora italiana           | 2020-03-05 12:15:45 |                   |
| **stato**                   | Stato di riferimento                | Country of reference            | ISO 3166-1 alpha-3 | ITA                  |
| **codice_regione**          | Codice della Regione (ISTAT 2019)   | Code of the Region (ISTAT 2019) | Number             | 13                   |
| **denominazione_regione**   | Denominazione della Regione         | Name of the Region              | Text string              | Abruzzo              |
| **codice_provincia**        | Codice della Provincia (ISTAT 2019) | Code of the Province            | Number             | 067                  |
| **denominazione_provincia** | Denominazione della provincia       | Name of the Province            | Text string              | Teramo               |
| **sigla_provincia**         | Sigla della Provincia               | Province abbreviation           | Text string              | TE                   |
| **lat**                     | Latitudine                          | Latitude                        | WGS84              | 42.6589177           |
| **long**                    | Longitudine                         | Longitude                       | WGS84              | 13.70439971          |
| **totale_casi**             | Totale casi positivi                | Total amount of positive cases  | Number             | 3                    |

*The autonomous provinces of Trento and Bolzano are indicated in "region designation" and with the Trentino Alto Adige code 04.*

*Each Region has a Province field called "In fase di definizione/aggiornamento" ("Being defined/updated") with the province code from 979 to 999, useful for indicating data not yet assigned to the Provinces.*

*An overall JSON file of all dates is available in the "data-json" folder: dpc-covid19-ita-province.json*

### National trend

**Directory:**  dati-andamento-nazionale

**Structure of the daily file:** dpc-covid19-ita-andamento-nazionale-yyyymmdd.csv (dpc-covid19-ita-andamento-nazionale-20200224.csv)

**Overall data file:** dpc-covid19-ita-andamento-nazionale.csv

| Field Name                  | Description (Italian)             | Description                            | Format                        | Example             |
|-----------------------------|-----------------------------------|----------------------------------------|-------------------------------|---------------------|
| **data**                        | Data dell’informazione            | Date of notification                   | YYYY-MM-DD HH:MM:SS (ISO 8601) Ora italiana | 2020-03-05 12:15:45 |
| **stato**                       | Stato di riferimento              | Country of reference                   | XYZ (ISO 3166-1 alpha-3)      | ITA                 |
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


*An overall JSON file of all dates is available in the "data-json" folder: dpc-covid19-ita-andamento-nazionale.json*

**License:** [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/deed.en) - [View license](https://github.com/pcm-dpc/COVID-19/blob/master/LICENSE)



**Dataset Editor/Author:** Italian Civil Protection Department

**Dataset subject:** [Salute umana e sicurezza - Human health and safety](http://inspire.ec.europa.eu/theme/hh) (Inspire)

**Category ISO 19115:** Health

*Data provided by the Italian Health Minister (Ministero della Salute)*

*Data processing and management by Italian Civil Protection Department*
