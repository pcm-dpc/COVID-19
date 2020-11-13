import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def get_categories( data, region, deaths=True, therapy=True, total=True ):
	# select by region
	subdata = data[ data["denominazione_regione"]==region ]
	# deaths per day
	res = []
	if deaths:
		deaths = subdata["deceduti"].values
		# compute deaths per day
		deaths = [deaths[0]] + \
					[ deaths[i]-deaths[i-1] for i in range(1,deaths.shape[0]) ]
		res.append( deaths )
	# intensive therapy per day
	if therapy:
		therapy = subdata["terapia_intensiva"].values
		res.append( therapy )
	# total positive cases
	if total:
		total = subdata["totale_positivi"].values
		res.append( total )

	return res



def plot_standard( axs, regions ):
	"""
	deaths and intensive therapies vs time. 
	"""
	for ax,region in zip(axs.flatten(),regions):
		d,t,p = regions[region]
		x = np.arange( len(d) )
		ax.plot( x, d, '.-', label='deceduti' )
		ax.plot( x, t, '.-', label='terapia intensiva' )
		ax.set_title( region )
		ax.legend()

def fexp( x, a, b, c ):
	return b * np.exp( a*x ) + c

def plot_loglinear( axs, regions ):
	"""
	deaths and intensive therapies vs time in log-linear. Fit exponentials.  
	"""
	last = len(regions["Lombardia"][0])
#	extrema_fit = {"Lombardia": [ [0,10], [160,220], [last-5,last] ], 
#						"Veneto": [ [0,30], [180,last] ], 
#						"Campania": [ [15,25], [200,last] ], 
#						"Marche": [ [5,15], [last-15,last] ], } 
	extrema_fit = {"Lombardia": [ [0,10] ], 
						"Veneto": [ [0,30] ], 
						"Campania": [ [15,25] ], 
						"Marche": [ [5,15] ], } 
	for ax,region in zip(axs.flatten(),regions):
		d,t,p = regions[region]
		x = np.arange( len(d) )
#		ax.plot( x, d, '.-', label='deceduti' )
		ax.plot( x, t, '.-', color='tab:orange', label='terapia intensiva' )
		ax.set_title( region )
		ax.set_yscale("log")
		ax.legend()
		# fit data
		for num,extrema in enumerate( extrema_fit[region] ):
			ex0,ex1 = extrema
			xx = x[ex0:ex1]
			tt = t[ex0:ex1]
			coeffs,_ = curve_fit( fexp, xx, tt, p0=[1,1,0] ) 
#			ax.plot( xx, fexp(xx, *coeffs), '--k' )
#			ax.annotate(	"a = {:.2f}".format(coeffs[0]), 
#								xy = (.5,.9 - .1*num), 
#								xycoords = 'axes fraction' )


# load all data
data = pd.read_csv( "dpc-covid19-ita-regioni.csv" )
# get deaths, intensive teraphy and total cases per day
regions = {"Lombardia":None, "Veneto":None, "Campania":None, "Marche":None}
deaths, therapies, positives = [], [], []
for region in regions:
	d,t,p = get_categories( data, region=region )
	regions[region] = [ d, t, p ]
# plot
fig, axs = plt.subplots(2,2)
plot_standard( axs, regions )
fig, axs = plt.subplots(2,2)
plot_loglinear( axs, regions )
plt.show()


