import csv
import matplotlib.pyplot as plt
from pylab import plot, xticks, yticks, title, xlabel, ylabel, savefig, ylim
import numpy as np

#import danych 

i_e_w = []

with open ('import_eksport_wartosc.csv',newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=';',quotechar='|')
    for row in data:
        i_e_w.append(row)

lata = []
surowce_energetyczne = []

for i in range (1,len(i_e_w)):
    lata.append (int(i_e_w [i][0]))
    surowce_energetyczne.append(float(i_e_w [i][2]))

lata=np.transpose(lata)
surowce_energetyczne=np.transpose(surowce_energetyczne)

fig = plt.figure()
ax = plt.subplot (111)
ax.bar(lata,surowce_energetyczne,width=1,color='b',edgecolor="r")

ylim(-60000,0)
xticks([2009,2010,2011,2012,2013,2014,2015,2016,2017,2018])
yticks([0,-5000,-10000,-15000,-20000,-25000,-30000,-35000,-40000,-45000,-50000,-55000,-60000])

title("SALDO WARTOŚCI EKSPORT - IMPORT SUROWCÓW MINERALNYCH W LATACH 2009 – 2018",fontsize=10) 
xlabel("Lata")  
ylabel("Surowce energetyczne")

plt.savefig("Projekt SQL.png", bbox_inches='tight')




    