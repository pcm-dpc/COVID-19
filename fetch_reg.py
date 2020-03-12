import json

regions = ["Abruzzo",
           "Basilicata",
           "Calabria",
           "Campania",
           "Emilia Romagna",
           "Friuli Venezia Giulia",
           "Lazio",
           "Liguria",
           "Lombardia",
           "Marche",
           "Molise",
           "Piemonte",
           "P.A. Bolzano",
           "P.A. Trento",
           "Puglia",
           "Sardegna",
           "Sicilia",
           "Toscana",
           "Umbria",
           "Valle d'Aosta",
           "Veneto"
           ]


def sanitize(string):
    return string.replace(" ", "").replace("'", "").replace(".", "").lower()


def data_of(reg):
    new = dict()
    with open('dati-json/dpc-covid19-ita-regioni.json') as json_file:
        data = json.load(json_file)
        filtered = []
        for thing in data:
            if thing['denominazione_regione'] == reg:
                filtered += [thing]
        with open('dati-json-regxreg/' + sanitize(reg) + '-data.json', 'w') as outfile:
            json.dump(filtered, outfile)


for rg in regions:
    data_of(rg)
