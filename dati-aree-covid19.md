<img src="http://opendatadpc.maps.arcgis.com/sharing/rest/content/items/5c8ef7516b5b4bb19f61037b4cd69015/data" alt="COVID-19" data-canonical-src="http://opendatadpc.maps.arcgis.com/sharing/rest/content/items/5c8ef7516b5b4bb19f61037b4cd69015/data" width="400" />

# Dati Aree misure di contenimento (Nazionali e Subregionali)

## Aggiornamento dei dati

- Dati Aree misure di contenimento (Nazionali e Subregionali): non pianificato e collegato alla pubblicazione dei relativi provvedimenti istitutivi (DPCM/Ordinanze regionali)

## Formato dei dati

- shape
- geojson

### Data Model "Area management/Restriction" Direttiva 2007/2/CE "INSPIRE"

**Directory:**  aree<br>
**Struttura file giornaliero: vedi seguito<br>
**File complessivo:**  dpc-covid-19-ita-aree e dpc-covid-19-ita-aree-comuni<br>

**Aree dove sono applicate misure restrittive a seguito di epidemia COVID-19**<br>
Aree nazionali, provinciali, comunali e/o subcomunali dove, in applicazione di specifici dispositivi giuridici, sono applicate misure restrittive per il contenimento dell'epidemia COVID-19 (per quelle subregionali ai sensi dell'art. 32, comma 3, della legge 23 dicembre 1978, n. 833 in materia di igiene e sanità pubblica).Si fa riferimento al Data Model del Tema n.11 Annex III "Zone sottoposte a gestione/limitazione/regolamentazione e unità con obbligo di comunicare i dati" della Direttiva 2007/2/CE Inspire.

| Nome campo | Descrizione |
|------------|-------------|
| **ID** | Identificatore univoco della singole feature del dataset. |
| **localId** | Identificatore univoco assegnato dal fornitore del dato nell'ambito nel namespace che identifica il fornitore del dataset.
| **namespace** | Nome che identifica univocamente il fornitore del dataset.
| **versionId** | Identificatore di una specifica versione della feature per definire un "ciclo di vita" dei provvedimenti a livello nazionale/regionale. Il valore è univoco all'interno dell'insieme di feature della medesima autorità competente ad emanare i provvedimenti (ad es. Regione).ESEMPIO: uno stesso comune o più comuni, nel tempo, sono assoggettati a misure restrittive con diversi provvedimenti. Ad ogni misura e ai territori da essa indicati è associata una specifica versione.
| **ThematicID** | Nome e identificatore del tema entro cui tutti I provvedimenti possono essere ricondotti. In questo caso si tratta di provvedimenti a livelo regionale presi durante la gestione emergenziale dell'epidemia da COVID 19.
| **Geographic Name** | Specifiche utilizzate per assegnare un nome geografico alle feature.
| **language** | Lingua utilizzata per il nome, attribuita con un codice di tre lettere, in accord con ISO 639-3 o ISO 639-5.
| **nameStatus** | Informazione qualitativa per comprendere il grado di standardizzazione da attribuire al nome utilizzato.
| **nativeness** | Informazione per comprendere se il nome adottato è quello effettivamente utilizzato nell'area a cui esso è riferito nel momento della sua utilizzazione.
| **pronunciation** | Pronuncia corretta del nome utilizzat0. In questo caso non è stato popolato perché ritenuto non necessario.
| **sourceOfName** | Fonte originale dei nomi geografici da cui sono stati integralmente presi.In questo caso sono stati adottati i nomi delle unità amministrative ISTAT.
| **spelling** | Modo in cui il nome è scritto e codice di lettere adottate per scriverlo.
| **Zone** | Insieme delle informazioni che specificano la classificazione della zone e altre informazioni ad essa relative.
| **zoneType** | Classificazione di alto livello per definire la zona a cui si applicano le misure restrittive. Il valore deriva da un vocabolario controllato. |
| **specializedZoneType** | Classificazione aggiuntiva per una ulteriore specificazione del tipo di zona.Il valore deriva da un vocabolario controllato. |
| **designationPeriod** | Intervallo temporale di applicazione delle misure restrittive definite legalmente con un provvedimento Regionale. Viene definito con una data di inizio e di fine.
| **environmentalDomain** | Classificazione del dominio ambientale per il quale l'adozione delle misure ha rappresentato il mezzo per ottenere specifici obiettivi di tutela.Il valore deriva da un vocabolario controllato.
| **beginLifespanVersion** | Data di inserimento o modifica della feature nel dataset.
| **endLifespanVersion** | Data in cui la feature è stata rimossa o dal dataset.
| **relatedParty** | Organizzazione che ha il ruolo di attribuzione delle misure restrittive.
| **organisationlName** | Nome dell'organizzazione. In questo caso si tratta dell'autorità che emana il provvedimento.
| **role** | Ruolo dell'organizzazione.
| **LegislationCitation Supertypes: DocumentCitation** | Citazione del provvedimento giuridico.
| **name** | Nome ufficiale del provvedimento (in taluni casi, per brevità è stata omessa una parte del nome ritenuta non indispensabile).
| **shortName** | Nome abbreviato o titolo alternativo del provvedimento.
| **date** | Data di creazione, pubblicazione o revisione del provvedimento.
| **link** | Link alla versione on line del provvedimento.
| **specificReference** | Riferimento ad una parte specifica del provvedimento.
| **identificationNumber** | Codice o sigla utilizzata per identificare il provvedimento (in genere si tratta della combinazione di numero e data).
| **officialDocumentNumber** | Numero che identifica univocamente il provvedimento (si è utilizzato il numero identificativo)
| **dateEnteredIntoForce** | Data di applicazione del provvedimento.
| **dateRepealed** | Data di abrogazione del provvedimento.
| **journalCitation** | Citazione del Bollettino Ufficiale della regione dove è pubblicato il provvedimento.
| **officialJournalIdentification** | Riferimento al Bollettino Ufficiale della Regione dove è pubblicato il provvedimento.Si è utilizzata la combinazione di numero e data di pubblicazione.
| **linkToJournal** | Link alla versione on line del Bollettino Ufficiale della regione dove è stato pubblicato il provvedimento.
<br><br><br>

### Licenza
**Licenza:** [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/deed.it) - [Visualizza licenza](https://github.com/pcm-dpc/COVID-19/blob/master/LICENSE)<br>
Scheda metadati RNDT: [aree](https://geodati.gov.it/geoportale/visualizzazione-metadati/scheda-metadati/?uuid=PCM%3A000086%3A20200306%3A110700)<br>
Scheda metadati RNDT: [aree](https://geodati.gov.it/geoportale/visualizzazione-metadati/scheda-metadati/?uuid=PCM:000086:20200420:120000)<br>
Tema del dataset: [Salute umana e sicurezza](http://inspire.ec.europa.eu/theme/hh) - [Human health and safety (Inspire)](http://inspire.ec.europa.eu/theme/hh)<br>
Tema del dataset: [Zone sottoposte a gestione/limitazioni/regolamentazione e unità con obbligo di comunicare dati](http://inspire.ec.europa.eu/theme/am) - [Area management / restriction / regulation zones & reporting units (Inspire)](http://inspire.ec.europa.eu/theme/am)<br>

Categoria ISO 19115: Salute e Pianificazione, Catasto<br> 
Dati elaborati dal Dipartimento della protezione civile a partire dai vari provvedimenti giuridici istitutivi<br>
Elaborazione e gestione dati a cura del Dipartimento della Protezione Civile