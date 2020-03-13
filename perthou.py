import json

# dati ISTAT 2019

regions = [{"nome": "Abruzzo", "abitanti": 1311580},
           {"nome": "Basilicata", "abitanti": 562869},
           {"nome": "Calabria", "abitanti": 1947131},
           {"nome": "Campania", "abitanti": 5801692},
           {"nome": "Emilia Romagna", "abitanti": 4459477},
           {"nome": "Friuli Venezia Giulia", "abitanti": 1215220},
           {"nome": "Lazio", "abitanti": 5879082},
           {"nome": "Liguria", "abitanti": 1550640},
           {"nome": "Lombardia", "abitanti": 10060574},
           {"nome": "Marche", "abitanti": 1525271},
           {"nome": "Molise", "abitanti": 305617},
           {"nome": "Piemonte", "abitanti": 4356406},
           {"nome": "P.A. Bolzano", "abitanti": 4029053},
           {"nome": "P.A. Trento", "abitanti": 1639591},
           {"nome": "Puglia", "abitanti": 4999891},
           {"nome": "Sardegna", "abitanti": 3729641},
           {"nome": "Sicilia", "abitanti": 541380},
           {"nome": "Toscana", "abitanti":},
           {"nome": "Umbria", "abitanti": 882015},
           {"nome": "Valle d'Aosta", "abitanti": 125666},
           {"nome": "Veneto", "abitanti": 4905854}
           ]


def perthou_nazionale(scale_factor):
    with open('dati-json/dpc-covid19-ita-andamento-nazionale.json') as json_file:
        data = json.load(json_file)
        for thing in data:
            thing["ricoverati_con_sintomi"] *= scale_factor
            thing["terapia_intensiva"] *= scale_factor
            thing["totale_ospedalizzati"] *= scale_factor
            thing["isolamento_domiciliare"] *= scale_factor
            thing["totale_attualmente_positivi"] *= scale_factor
            thing["nuovi_attualmente_positivi"] *= scale_factor
            thing["dimessi_guariti"] *= scale_factor
            thing["deceduti"] *= scale_factor
            thing["totale_casi"] *= scale_factor
            thing["tamponi"] *= scale_factor
        with open('dati-json/dpc-covid19-ita-andamento-nazionale-permille.json', 'w') as outfile:
            json.dump(data, outfile)


perthou_nazionale(1000/60483973)
