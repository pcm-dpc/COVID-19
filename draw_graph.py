#!/usr/bin/python3

import matplotlib.pyplot as plt
import csv

from math import atan2,degrees
import numpy as np

#Label line with line2D label data
def labelLine(line,x,label=None,align=True,**kwargs):

    ax = line.axes
    xdata = line.get_xdata()
    ydata = line.get_ydata()

    if (x < xdata[0]) or (x > xdata[-1]):
        print('x label location is outside data range!')
        return

    #Find corresponding y co-ordinate and angle of the line
    ip = 1
    for i in range(len(xdata)):
        if x < xdata[i]:
            ip = i
            break

    y = ydata[ip-1] + (ydata[ip]-ydata[ip-1])*(x-xdata[ip-1])/(xdata[ip]-xdata[ip-1])

    if not label:
        label = line.get_label()

    if align:
        #Compute the slope
        dx = xdata[ip] - xdata[ip-1]
        dy = ydata[ip] - ydata[ip-1]
        ang = degrees(atan2(dy,dx))

        #Transform to screen co-ordinates
        pt = np.array([x,y]).reshape((1,2))
        trans_angle = ax.transData.transform_angles(np.array((ang,)),pt)[0]

    else:
        trans_angle = 0

    #Set a bunch of keyword arguments
    if 'color' not in kwargs:
        kwargs['color'] = line.get_color()

    if ('horizontalalignment' not in kwargs) and ('ha' not in kwargs):
        kwargs['ha'] = 'center'

    if ('verticalalignment' not in kwargs) and ('va' not in kwargs):
        kwargs['va'] = 'center'

    if 'backgroundcolor' not in kwargs:
        kwargs['backgroundcolor'] = ax.get_facecolor()

    if 'clip_on' not in kwargs:
        kwargs['clip_on'] = True

    if 'zorder' not in kwargs:
        kwargs['zorder'] = 2.5

    ax.text(x,y,label,rotation=trans_angle,**kwargs)

def labelLines(lines,align=True,xvals=None,**kwargs):

    ax = lines[0].axes
    labLines = []
    labels = []

    #Take only the lines which have labels other than the default ones
    for line in lines:
        label = line.get_label()
        if "_line" not in label:
            labLines.append(line)
            labels.append(label)

    if xvals is None:
        xmin,xmax = ax.get_xlim()
        xvals = np.linspace(xmin,xmax,len(labLines)+2)[5:-5]

    for line,x,label in zip(labLines,xvals,labels):
        labelLine(line,x,label,align,**kwargs)


def create_graphic(name,file_path,column_key,exclude,operation_fun):
        x_out={}   
        y_out={}

        with open(file_path, 'r') as csvfile:
                plots= csv.DictReader(csvfile, delimiter=',')
                for row in plots:
                        if row[column_key] not in exclude:
                                value = operation_fun(row)
                                if row[column_key] in y_out:
                                        y_out[row[column_key]].append(value)
                                        x_out[row[column_key]].append(len(x_out[row[column_key]]))
                                else:
                                        y_out[row[column_key]] = [value]
                                        x_out[row[column_key]] = [0]

        plt.figure(name)

        for key,value in y_out.items():
                plt.plot(x_out[key],value,marker='o',label=key)

        labelLines(plt.gca().get_lines(),zorder=2.5)
        
        #plt.legend()

        plt.title('COVID 19')

        plt.xlabel('Days')
        plt.ylabel('People')

        plt.show(False)

### Main

exclude_region = []
exclude_province = ["In fase di definizione/aggiornamento"]

fun_totale_casi = lambda row : int(row['totale_casi'])
fun_percentuale_guariti = lambda row: int(row['dimessi_guariti']) / int(row['totale_casi']) if int(row['totale_casi']) != 0 else 0

create_graphic("Regioni",'dati-regioni/dpc-covid19-ita-regioni.csv','denominazione_regione',exclude_region, fun_totale_casi)
create_graphic("Province",'dati-province/dpc-covid19-ita-province.csv','denominazione_provincia',exclude_province, fun_totale_casi)
create_graphic("Nazionale",'dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv','stato',[], fun_totale_casi)  
create_graphic("Regioni Guariti / Totale Casi",'dati-regioni/dpc-covid19-ita-regioni.csv','denominazione_regione',exclude_region,fun_percentuale_guariti)


input("Press Enter to close...")

### End
