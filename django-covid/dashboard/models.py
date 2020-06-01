from django.db import models

# ref: https://docs.djangoproject.com/en/3.0/intro/tutorial02/

from django.db import models

# ref: https://docs.djangoproject.com/en/3.0/ref/models/fields/


# data,stato,ricoverati_con_sintomi,terapia_intensiva,totale_ospedalizzati,isolamento_domiciliare,totale_positivi,variazione_totale_positivi,nuovi_positivi,dimessi_guariti,deceduti,totale_casi,tamponi,casi_testati,note_it,note_en
class Nazione(models.Model):
    data = models.CharField(max_length=20, unique=True)
    stato = models.CharField(max_length=3)
    ricoverati_con_sintomi = models.IntegerField(null=True)
    terapia_intensiva = models.IntegerField(null=True)
    totale_ospedalizzati = models.IntegerField(null=True)
    isolamento_domiciliare = models.IntegerField(null=True)
    totale_positivi = models.IntegerField(null=True)
    variazione_totale_positivi = models.IntegerField(null=True)
    nuovi_positivi = models.IntegerField(null=True)
    dimessi_guariti = models.IntegerField(null=True)
    deceduti = models.IntegerField(null=True)
    totale_casi = models.IntegerField(null=True)
    tamponi = models.IntegerField(null=True)
    casi_testati = models.IntegerField(null=True)
    note_it = models.TextField(null=True)
    note_en = models.TextField(null=True)


# data,stato,codice_regione,denominazione_regione,lat,long,ricoverati_con_sintomi,terapia_intensiva,totale_ospedalizzati,isolamento_domiciliare,totale_positivi,variazione_totale_positivi,nuovi_positivi,dimessi_guariti,deceduti,totale_casi,tamponi,casi_testati,note_it,note_en
class Regione(models.Model):
    data = models.CharField(max_length=20)
    stato = models.CharField(max_length=3)
    codice_regione = models.IntegerField()
    denominazione_regione = models.CharField(max_length=40)
    lat = models.CharField(max_length=20)
    long = models.CharField(max_length=20)
    ricoverati_con_sintomi = models.IntegerField(null=True)
    terapia_intensiva = models.IntegerField(null=True)
    totale_ospedalizzati = models.IntegerField(null=True)
    isolamento_domiciliare = models.IntegerField(null=True)
    totale_positivi = models.IntegerField(null=True)
    variazione_totale_positivi = models.IntegerField(null=True)
    nuovi_positivi = models.IntegerField(null=True)
    dimessi_guariti = models.IntegerField(null=True)
    deceduti = models.IntegerField(null=True)
    totale_casi = models.IntegerField(null=True)
    tamponi = models.IntegerField(null=True)
    casi_testati = models.IntegerField(null=True)
    note_it = models.TextField(null=True)
    note_en = models.TextField(null=True)

    class Meta:
        unique_together = (("data", "codice_regione"),) # pseudo-composite key


class Provincia(models.Model):
    data = models.CharField(max_length=20)
    stato = models.CharField(max_length=3)
    codice_regione = models.IntegerField()
    denominazione_regione = models.CharField(max_length=40)
    codice_provincia = models.CharField(max_length=40)
    denominazione_provincia = models.CharField(max_length=40)
    sigla_provincia = models.CharField(max_length=40)
    lat = models.CharField(max_length=20)
    long = models.CharField(max_length=20)
    totale_casi = models.IntegerField(null=True)
    note_it = models.TextField(null=True)
    note_en = models.TextField(null=True)

    class Meta:
        unique_together = (("data", "codice_provincia"),) # pseudo-composite key