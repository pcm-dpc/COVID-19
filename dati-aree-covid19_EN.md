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

**Areas where restrictive measures are applied following the COVID-19 epidemic**<br>
National, provincial, municipal and / or sub-municipal areas where, in application of specific legal provisions, restrictive measures are applied for the containment of the COVID-19 epidemic (for sub-regional ones pursuant to art.32, paragraph 3, of law 23 833 of December 1978 on hygiene and public health). Reference is made to the Data Model of Theme 11 Annex III "Areas subject to management / limitation / regulation and units with obligation to communicate data" of Directive 2007 / 2 / CE Inspire.

| Nome campo | Descrizione |
|------------|-------------|
| **ID** | Unique identifier of the individual features of the dataset.
| **localId** | Unique identifier assigned by the data provider in the namespace that identifies the supplier of the dataset.
| **namespace** | Name that uniquely identifies the provider of the dataset.
| **versionId** | Identifier of a specific version of the feature to define a "life cycle" of the measures at national/regional level. The value is unique within the set of features of the same competent authority to issue the measures (i.e. Region). EXAMPLE: the same municipality or more municipalities, over time, are subject to restrictive measures with different measures. A specific version is associated with each measure and the territories indicated by it.
| **ThematicID** | Name and identifier of the topic within which all the measures can be traced. In this case, these are regional measures taken during the emergency management of the COVID epidemic 19.
| **Geographic Name** | Specification used to name features geographically.
| **language** | Language used for the name, attributed with a three letter code, in accordance with ISO 639-3 or ISO 639-5.
| **nameStatus** | Qualitative information to understand the degree of standardization to be attributed to the name used.
| **nativeness** | Information to understand if the name adopted is the one actually used in the area to which it refers at the time of its use.
| **pronunciation** | Correct pronunciation of the name used. In this case it was not populated because it was deemed unnecessary.
| **sourceOfName** | Original source of the geographic names from which they were taken in full, in this case the names of the ISTAT administrative units were adopted.
| **spelling** | How the name is written and code of letters taken to write it.
| **Zone** | Set of information specifying the classification of the zone and other related information.
| **zoneType** | High level classification to define the area to which the restrictive measures apply. The value comes from a controlled vocabulary.
| **specializedZoneType** | Additional classification for further specification of the type of zone. The value derives from a controlled vocabulary.
| **designationPeriod** | Time interval of application of the restrictive measures legally defined with a Regional provision. It is defined with a start and end date.
| **environmentalDomain** | Classification of the environmental domain for which the adoption of measures represented the means to achieve specific protection objectives. The value derives from a controlled vocabulary.
| **beginLifespanVersion** | Date of insertion or modification of the feature in the dataset.
| **endLifespanVersion** | Date the feature was removed or from the dataset.
| **relatedParty** | Organization that has the role of attributing restrictive measures.
| **organisationlName** | Nome dell'organizzazione. In questo caso si tratta dell'autorità che emana il provvedimento.
| **role** | Role of the organization.
| **LegislationCitation Supertypes: DocumentCitation** | Citation of the legal provision.
| **name** | Official name of the measure (in some cases, for brevity a part of the name deemed non-essential has been omitted).
| **shortName** | Abbreviated name or alternative title of the measure.
| **date** | Date of creation, publication or revision of the provision.
| **link** | Link to the online version of the measure.
| **specificReference** | Reference to a specific part of the measure.
| **identificationNumber** | Code or abbreviation used to identify the measure (generally it is the combination of number and date).
| **officialDocumentNumber** | Number that uniquely identifies the measure (the identification number has been used).
| **dateEnteredIntoForce** | Date of application of the measure.
| **dateRepealed** | Date of repeal of the provision.
| **journalCitation** | Citation of the Official Bulletin of the region where the measure is published.
| **officialJournalIdentification** | Citation of the Official Bulletin of the region where the measure is published.
| **linkToJournal** | Link to the online version of the Official Bulletin of the region where the measure was published.
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