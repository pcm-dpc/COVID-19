import numpy as np
import pandas as pd
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


# load all data
data = pd.read_csv( "dpc-covid19-ita-regioni.csv" )
# get deaths, intensive teraphy and total cases per day
d,t,p = get_categories( data, region="Lombardia" )
# plot
x = np.arange( len(d) )
plt.plot( x, d, label='deceduti' )
plt.plot( x, t, label='terapia intensiva' )
#plt.plot( x, p, label='casi positivi' )
plt.legend()
plt.show()
