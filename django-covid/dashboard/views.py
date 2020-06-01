from django.shortcuts import render

# ref: https://docs.djangoproject.com/en/3.0/intro/tutorial03/

from django.http import HttpResponse
from django.core import serializers
from dashboard.models import Regione, Nazione, Provincia


def calculateDetailsForState():
    labels = set()
    ricoverati_con_sintomi = []
    terapia_intensiva = []
    totale_ospedalizzati = []
    isolamento_domiciliare = []
    attualmente_positivi = []
    dimessi_guariti = []
    deceduti = []
    totale_casi = []
    tamponi = []
    perc_casi_conclusi = []
    perc_guariti = []
    perc_successo = []
    nuovi_tamponi = []
    nuovi_positivi = []
    nuovi_guariti = []
    nuovi_deceduti = []
    perc_nuovi_positivi_per_tamponi = []

    # regions = Regione.objects.all()
    ita = Nazione.objects.all().order_by('data')

    # init
    first = ita.first()
    positivi_ieri = first.totale_casi
    guariti_ieri = first.dimessi_guariti
    deceduti_ieri = first.deceduti
    tamponi_ieri = first.tamponi

    for r in ita:
        labels.add(r.data)  # store all distinct date values

        casi_conclusi_oggi = r.dimessi_guariti + r.deceduti

        if (r.totale_casi > 0):
            perc_casi_conclusi_oggi = casi_conclusi_oggi / r.totale_casi
            perc_guariti_oggi = r.dimessi_guariti / r.totale_casi
        else:
            perc_casi_conclusi_oggi = 0
            perc_guariti_oggi = 0

        if (casi_conclusi_oggi > 0):
            perc_successo_oggi = r.dimessi_guariti / casi_conclusi_oggi
        else:
            perc_successo_oggi = 0

        nuovi_tamponi_oggi = r.tamponi - tamponi_ieri
        nuovi_positivi_oggi = r.totale_casi - positivi_ieri
        nuovi_guariti_oggi = r.dimessi_guariti - guariti_ieri
        nuovi_deceduti_oggi = r.deceduti - deceduti_ieri

        if (nuovi_tamponi_oggi > 0):
            perc_nuovi_positivi_per_tamponi_oggi = nuovi_positivi_oggi / nuovi_tamponi_oggi
        else:
            perc_nuovi_positivi_per_tamponi_oggi = 0

        ricoverati_con_sintomi.append(r.ricoverati_con_sintomi)
        terapia_intensiva.append(r.terapia_intensiva)
        totale_ospedalizzati.append(r.totale_ospedalizzati)
        isolamento_domiciliare.append(r.isolamento_domiciliare)
        attualmente_positivi.append(r.totale_positivi)
        dimessi_guariti.append(r.dimessi_guariti)
        deceduti.append(r.deceduti)
        totale_casi.append(r.totale_casi)
        tamponi.append(r.tamponi)
        perc_casi_conclusi.append(perc_casi_conclusi_oggi * 100)
        perc_guariti.append(perc_guariti_oggi * 100)
        perc_successo.append(perc_successo_oggi * 100)
        nuovi_tamponi.append(nuovi_tamponi_oggi)
        nuovi_positivi.append(nuovi_positivi_oggi)
        nuovi_guariti.append(nuovi_guariti_oggi)
        nuovi_deceduti.append(nuovi_deceduti_oggi)
        perc_nuovi_positivi_per_tamponi.append(perc_nuovi_positivi_per_tamponi_oggi * 100)

        positivi_ieri = r.totale_casi
        guariti_ieri = r.dimessi_guariti
        deceduti_ieri = r.deceduti
        tamponi_ieri = r.tamponi

    labels = sorted(labels)

    result = {
        "labels": labels,
        "ricoverati_con_sintomi": ricoverati_con_sintomi,
        "terapia_intensiva": terapia_intensiva,
        "totale_ospedalizzati": totale_ospedalizzati,
        "isolamento_domiciliare": isolamento_domiciliare,
        "attualmente_positivi": attualmente_positivi,
        "dimessi_guariti": dimessi_guariti,
        "deceduti": deceduti,
        "totale_casi": totale_casi,
        "tamponi": tamponi,
        "perc_casi_conclusi": perc_casi_conclusi,
        "perc_guariti": perc_guariti,
        "perc_successo": perc_successo,
        "nuovi_tamponi": nuovi_tamponi,
        "nuovi_positivi": nuovi_positivi,
        "nuovi_guariti": nuovi_guariti,
        "nuovi_deceduti": nuovi_deceduti,
        "perc_nuovi_positivi_per_tamponi": perc_nuovi_positivi_per_tamponi,
    }

    return result


def calculateDetailsForRegion(regionCode):
    labels = set()
    ricoverati_con_sintomi = []
    terapia_intensiva = []
    totale_ospedalizzati = []
    isolamento_domiciliare = []
    attualmente_positivi = []
    dimessi_guariti = []
    deceduti = []
    totale_casi = []
    tamponi = []
    perc_casi_conclusi = []
    perc_guariti = []
    perc_successo = []
    nuovi_tamponi = []
    nuovi_positivi = []
    nuovi_guariti = []
    nuovi_deceduti = []
    perc_nuovi_positivi_per_tamponi = []

    # regions = Regione.objects.all()
    region = Regione.objects.filter(codice_regione=regionCode).order_by('data')

    # init
    first = region.first()
    regionName = first.denominazione_regione
    positivi_ieri = first.totale_casi
    guariti_ieri = first.dimessi_guariti
    deceduti_ieri = first.deceduti
    tamponi_ieri = first.tamponi

    for r in region:
        labels.add(r.data)  # store all distinct date values

        casi_conclusi_oggi = r.dimessi_guariti + r.deceduti

        if (r.totale_casi > 0):
            perc_casi_conclusi_oggi = casi_conclusi_oggi / r.totale_casi
            perc_guariti_oggi = r.dimessi_guariti / r.totale_casi
        else:
            perc_casi_conclusi_oggi = 0
            perc_guariti_oggi = 0

        if (casi_conclusi_oggi > 0):
            perc_successo_oggi = r.dimessi_guariti / casi_conclusi_oggi
        else:
            perc_successo_oggi = 0

        nuovi_tamponi_oggi = r.tamponi - tamponi_ieri
        nuovi_positivi_oggi = r.totale_casi - positivi_ieri
        nuovi_guariti_oggi = r.dimessi_guariti - guariti_ieri
        nuovi_deceduti_oggi = r.deceduti - deceduti_ieri

        if (nuovi_tamponi_oggi > 0):
            perc_nuovi_positivi_per_tamponi_oggi = nuovi_positivi_oggi / nuovi_tamponi_oggi
        else:
            perc_nuovi_positivi_per_tamponi_oggi = 0

        ricoverati_con_sintomi.append(r.ricoverati_con_sintomi)
        terapia_intensiva.append(r.terapia_intensiva)
        totale_ospedalizzati.append(r.totale_ospedalizzati)
        isolamento_domiciliare.append(r.isolamento_domiciliare)
        attualmente_positivi.append(r.totale_positivi)
        dimessi_guariti.append(r.dimessi_guariti)
        deceduti.append(r.deceduti)
        totale_casi.append(r.totale_casi)
        tamponi.append(r.tamponi)
        perc_casi_conclusi.append(perc_casi_conclusi_oggi * 100)
        perc_guariti.append(perc_guariti_oggi * 100)
        perc_successo.append(perc_successo_oggi * 100)
        nuovi_tamponi.append(nuovi_tamponi_oggi)
        nuovi_positivi.append(nuovi_positivi_oggi)
        nuovi_guariti.append(nuovi_guariti_oggi)
        nuovi_deceduti.append(nuovi_deceduti_oggi)
        perc_nuovi_positivi_per_tamponi.append(perc_nuovi_positivi_per_tamponi_oggi * 100)

        positivi_ieri = r.totale_casi
        guariti_ieri = r.dimessi_guariti
        deceduti_ieri = r.deceduti
        tamponi_ieri = r.tamponi

    labels = sorted(labels)

    result = {
        "regionName": regionName,
        "labels": labels,
        "ricoverati_con_sintomi": ricoverati_con_sintomi,
        "terapia_intensiva": terapia_intensiva,
        "totale_ospedalizzati": totale_ospedalizzati,
        "isolamento_domiciliare": isolamento_domiciliare,
        "attualmente_positivi": attualmente_positivi,
        "dimessi_guariti": dimessi_guariti,
        "deceduti": deceduti,
        "totale_casi": totale_casi,
        "tamponi": tamponi,
        "perc_casi_conclusi": perc_casi_conclusi,
        "perc_guariti": perc_guariti,
        "perc_successo": perc_successo,
        "nuovi_tamponi": nuovi_tamponi,
        "nuovi_positivi": nuovi_positivi,
        "nuovi_guariti": nuovi_guariti,
        "nuovi_deceduti": nuovi_deceduti,
        "perc_nuovi_positivi_per_tamponi": perc_nuovi_positivi_per_tamponi,
    }

    province = Provincia.objects.filter(codice_regione=regionCode).order_by('data').values()    # list of Provincia dicts

    return result


def graph(request):

    # check if the passed value is an integer
    if request.method == 'POST' and 'regionCode' in request.POST:
        try:
            int(request.POST['regionCode'])
        except ValueError:
            return

    regionCode = request.POST['regionCode']
    # print(regionCode)
    result = calculateDetailsForRegion(regionCode)

    # print(result)

    return render(request, "dashboard/graph.html", result)


def home(request):

    if request.method == 'POST' and 'regionCode' in request.POST:
        return graph(request)

    regions = []
    regionsWithDifferentCode = Regione.objects.all().distinct('codice_regione')
    for region in regionsWithDifferentCode:
        regions.append({'code': region.codice_regione, 'name': region.denominazione_regione})

    def sort_key(e):
        return e['name']

    regions.sort(key=sort_key)

    # sorted_regions = sorted(regions.items(), key=lambda x: x[1])
    ita = calculateDetailsForState()
    ita["regions"] = regions

    return render(request, "dashboard/home.html", ita)