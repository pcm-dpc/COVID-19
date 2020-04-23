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
**File complessivo:**  	dpc-covid-19-ita-aree e  	dpc-covid-19-ita-aree-comuni <br>


| **Aree dove sono applicate misure restrittive a seguito di epidemia COVID-19** | Aree nazionali, provinciali, comunali e/o subcomunali dove, in applicazione di specifici dispositivi giuridici, sono applicate misure restrittive per il contenimento dell'epidemia COVID-19 (per quelle subregionali ai sensi dell'art. 32, comma 3, della legge 23 dicembre 1978, n. 833 in materia di igiene e sanità pubblica).Si fa riferimento al Data Model del Tema n.11 Annex III "Zone sottoposte a gestione/limitazione/regolamentazione e unità con obbligo di comunicare i dati" della Direttiva 2007/2/CE Inspire. |
| --- 
| **ID** | Identificatore univoco della singole feature del dataset. |
| **localId** | Identificatore univoco assegnato dal fornitore del dato nell'ambito nel namespace che identifica il fornitore del dataset. |
| **namespace** | Nome che identifica univocamente il fornitore del dataset. |
| **versionId** | Identificatore di una specifica versione della feature per definire un "ciclo di vita" dei provvedimenti a livello nazionale/regionale. Il valore è univoco all'interno dell'insieme di feature della medesima autorità competente ad emanare i provvedimenti (ad es. Regione).ESEMPIO: uno stesso comune o più comuni, nel tempo, sono assoggettati a misure restrittive con diversi provvedimenti. Ad ogni misura e ai territori da essa indicati è associata una specifica versione. |
| **ThematicID** | Nome e identificatore del tema entro cui tutti I provvedimenti possono essere ricondotti. In questo caso si tratta di provvedimenti a livelo regionale presi durante la gestione emergenziale dell'epidemia da COVID 19. |
| --- 
| **Geographic Name** | Specifiche utilizzate per assegnare un nome geografico alle feature. |
| --- 
| **language** | Lingua utilizzata per il nome, attribuita con un codice di tre lettere, in accord con ISO 639-3 o ISO 639-5. |
| **nameStatus** | Informazione qualitativa per comprendere il grado di standardizzazione da attribuire al nome utilizzato. |
| **nativeness** | Informazione per comprendere se il nome adottato è quello effettivamente utilizzato nell'area a cui esso è riferito nel momento della sua utilizzazione.|
| **pronunciation** | Pronuncia corretta del nome utilizzat0. In questo caso non è stato popolato perché ritenuto non necessario. |
| **sourceOfName** | Fonte originale dei nomi geografici da cui sono stati integralmente presi.In questo caso sono stati adottati i nomi delle unità amministrative ISTAT. |
| **spelling** | Modo in cui il nome è scritto e codice di lettere adottate per scriverlo. |
| --- 
| **Zone** | Insieme delle informazioni che specificano la classificazione della zone e altre informazioni ad essa relative. |
| --- 
| **zoneType** | Classificazione di alto livello per definire la zona a cui si applicano le misure restrittive. Il valore deriva da un vocabolario controllato. |
| **specializedZoneType** | Classificazione aggiuntiva per una ulteriore specificazione del tipo di zona.Il valore deriva da un vocabolario controllato. |
| **designationPeriod** | Intervallo temporale di applicazione delle misure restrittive definite legalmente con un provvedimento Regionale. Viene definito con una data di inizio e di fine. |
| **environmentalDomain** | Classificazione del dominio ambientale per il quale l'adozione delle misure ha rappresentato il mezzo per ottenere specifici obiettivi di tutela.Il valore deriva da un vocabolario controllato. |
| **beginLifespanVersion** | Data di inserimento o modifica della feature nel dataset. |
| **endLifespanVersion** | Data in cui la feature è stata rimossa o dal dataset. |
| --- 
| **relatedParty** | Organizzazione che ha il ruolo di attribuzione delle misure restrittive. |
| **organisationlName** | Nome dell'organizzazione. In questo caso si tratta dell'autorità che emana il provvedimento. |
| **role** | Ruolo dell'organizzazione. |
| --- 
| **LegislationCitation Supertypes: DocumentCitation** | Citazione del provvedimento giuridico. |
| --- 
| **name** | Nome ufficiale del provvedimento (in taluni casi, per brevità è stata omessa una parte del nome ritenuta non indispensabile). |
| **shortName** | Nome abbreviato o titolo alternativo del provvedimento. |
| **date** | Data di creazione, pubblicazione o revisione del provvedimento. |
| **link** | Link alla versione on line del provvedimento. |
| **specificReference** | Riferimento ad una parte specifica del provvedimento. |
| **identificationNumber** | Codice o sigla utilizzata per identificare il provvedimento (in genere si tratta della combinazione di numero e data). |
| **officialDocumentNumber** | Numero che identifica univocamente il provvedimento (si è utilizzato il numero identificativo) |
| **dateEnteredIntoForce** | Data di applicazione del provvedimento. |
| **dateRepealed** | Data di abrogazione del provvedimento.. |
| --- 
| **journalCitation** | Citazione del Bollettino Ufficiale della regione dove è pubblicato il provvedimento.. |
| --- 
| **officialJournalIdentification** | Riferimento al Bollettino Ufficiale della Regione dove è pubblicato il provvedimento.Si è utilizzata la combinazione di numero e data di pubblicazione. |
| **linkToJournal** | Link alla versione on line del Bollettino Ufficiale della regione dove è stato pubblicato il provvedimento. |

| **Areas where restrictive measures are applied following the COVID-19 epidemic ** | National, provincial, municipal and / or sub-municipal areas where, in application of specific legal provisions, restrictive measures are applied for the containment of the COVID-19 epidemic (for sub-regional ones pursuant to art.32, paragraph 3, of law 23 833 of December 1978 on hygiene and public health). Reference is made to the Data Model of Theme 11 Annex III "Areas subject to management / limitation / regulation and units with obligation to communicate data" of Directive 2007 / 2 / CE Inspire. |
| --- 
| **ID** | Unique identifier of the individual features of the dataset. |
| **localId** | Unique identifier assigned by the data provider in the namespace that identifies the supplier of the dataset. |
| **namespace** | Name that uniquely identifies the provider of the dataset. |
| **versionId** | Identifier of a specific version of the feature to define a "life cycle" of the measures at national/regional level. The value is unique within the set of features of the same competent authority to issue the measures (i.e. Region). EXAMPLE: the same municipality or more municipalities, over time, are subject to restrictive measures with different measures. A specific version is associated with each measure and the territories indicated by it. |
| **ThematicID** | Name and identifier of the topic within which all the measures can be traced. In this case, these are regional measures taken during the emergency management of the COVID epidemic 19. |
| --- 
| **Geographic Name** | Specification used to name features geographically. |
| --- 
| **language** | Language used for the name, attributed with a three letter code, in accordance with ISO 639-3 or ISO 639-5. |
| **nameStatus** | Qualitative information to understand the degree of standardization to be attributed to the name used.|
| **nativeness** | Information to understand if the name adopted is the one actually used in the area to which it refers at the time of its use.|
| **pronunciation** | Correct pronunciation of the name used. In this case it was not populated because it was deemed unnecessary.|
| **sourceOfName** | Original source of the geographic names from which they were taken in full, in this case the names of the ISTAT administrative units were adopted. |
| **spelling** | How the name is written and code of letters taken to write it. |
| --- 
| **Zone** | Set of information specifying the classification of the zone and other related information. |
| --- 
| **zoneType** | High level classification to define the area to which the restrictive measures apply. The value comes from a controlled vocabulary. |
| **specializedZoneType** | Additional classification for further specification of the type of zone. The value derives from a controlled vocabulary. |
| **designationPeriod** | Time interval of application of the restrictive measures legally defined with a Regional provision. It is defined with a start and end date. |
| **environmentalDomain** | Classification of the environmental domain for which the adoption of measures represented the means to achieve specific protection objectives. The value derives from a controlled vocabulary. |
| **beginLifespanVersion** | Date of insertion or modification of the feature in the dataset.
|
| **endLifespanVersion** | Date the feature was removed or from the dataset.|
| --- 
| **relatedParty** | Organization that has the role of attributing restrictive measures. |
| **organisationlName** | Nome dell'organizzazione. In questo caso si tratta dell'autorità che emana il provvedimento. |
| **role** | Role of the organization. |
| --- 
| **LegislationCitation Supertypes: DocumentCitation** | Citation of the legal provision. |
| --- 
| **name** | Official name of the measure (in some cases, for brevity a part of the name deemed non-essential has been omitted). |
| **shortName** | Abbreviated name or alternative title of the measure. |
| **date** | Date of creation, publication or revision of the provision. |
| **link** | Link to the online version of the measure. |
| **specificReference** | Reference to a specific part of the measure. |
| **identificationNumber** | Code or abbreviation used to identify the measure (generally it is the combination of number and date). |
| **officialDocumentNumber** | Number that uniquely identifies the measure (the identification number has been used). |
| **dateEnteredIntoForce** | Date of application of the measure. |
| **dateRepealed** | Date of repeal of the provision. |
| --- 
| **journalCitation** | Citation of the Official Bulletin of the region where the measure is published. |
| --- 
| **officialJournalIdentification** | Citation of the Official Bulletin of the region where the measure is published. |
| **linkToJournal** | Link to the online version of the Official Bulletin of the region where the measure was published. |

### Licenza
**Licenza:** [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/deed.it) - [Visualizza licenza](https://github.com/pcm-dpc/COVID-19/blob/master/LICENSE)<br>
Scheda metadati RNDT: [aree](https://geodati.gov.it/geoportale/visualizzazione-metadati/scheda-metadati/?uuid=PCM%3A000086%3A20200306%3A110700)<br>
Scheda metadati RNDT: [aree](https://geodati.gov.it/geoportale/visualizzazione-metadati/scheda-metadati/?uuid=PCM:000086:20200420:120000)<br>
Tema del dataset: [Salute umana e sicurezza](http://inspire.ec.europa.eu/theme/hh) - [Human health and safety (Inspire)](http://inspire.ec.europa.eu/theme/hh)<br>
Tema del dataset: [Zone sottoposte a gestione/limitazioni/regolamentazione e unità con obbligo di comunicare dati](http://inspire.ec.europa.eu/theme/am) - [Area management / restriction / regulation zones & reporting units (Inspire)](http://inspire.ec.europa.eu/theme/am)<br>

Categoria ISO 19115: Salute e Pianificazione, Catasto<br> 
Dati elaborati dal Dipartimento della protezione civile a partire dai vari provvedimenti giuridici istitutivi<br>
Elaborazione e gestione dati a cura del Dipartimento della Protezione Civile