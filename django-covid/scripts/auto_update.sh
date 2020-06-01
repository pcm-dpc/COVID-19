#!/bin/bash
DATA_DIR=../../
REGION_DIR=$DATA_DIR/dati-regioni
PROVINCE_DIR=$DATA_DIR/dati-province
NAZIONE_DIR=$DATA_DIR/dati-andamento-nazionale

TODAY=$(date +"%Y%m%d")

cd $DATA_DIR
sudo su covid git pull

psql -d covid -c "\COPY dashboard_regione(data,stato,codice_regione,denominazione_regione,lat,long,ricoverati_con_sintomi,terapia_intensiva,totale_ospedalizzati,isolamento_domiciliare,totale_positivi,variazione_totale_positivi,nuovi_positivi,dimessi_guariti,deceduti,totale_casi,tamponi,casi_testati,note_it,note_en) FROM '$REGION_DIR/dpc-covid19-ita-regioni-$TODAY.csv' DELIMITER ',' CSV HEADER;"
# psql -d covid -c "\COPY dashboard_provincia(data,stato,codice_regione,denominazione_regione,codice_provincia,denominazione_provincia,sigla_provincia,lat,long,totale_casi,note_it,note_en) FROM '$PROVINCE_DIR/dpc-covid19-ita-province-$TODAY.csv' DELIMITER ',' CSV HEADER;"
psql -d covid -c "\COPY dashboard_nazione(data,stato,ricoverati_con_sintomi,terapia_intensiva,totale_ospedalizzati,isolamento_domiciliare,totale_positivi,variazione_totale_positivi,nuovi_positivi,dimessi_guariti,deceduti,totale_casi,tamponi,casi_testati,note_it,note_en) FROM '$NAZIONE_DIR/dpc-covid19-ita-andamento-nazionale-$TODAY.csv' DELIMITER ',' CSV HEADER;"
