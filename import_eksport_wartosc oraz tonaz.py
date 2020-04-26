import csv
import matplotlib.pyplot as plt
from pylab import plot, xticks, yticks, title, xlabel, ylabel, savefig, ylim
import numpy as np

#IMPORT DANYCH 

#saldo wartosci eksport - import 

i_e_w = []

with open ('import_eksport_wartosc.csv',newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=';',quotechar='|')
    for row in data:
        i_e_w.append(row)
        
#saldo tonazu eksport - import 

i_e_t = []

with open ('import_eksport_tonaz.csv',newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=';',quotechar='|')
    for row in data:
        i_e_t.append(row)
        

        
#WYCIAGANIE DANYCH
    
#saldo wartosci eksport - import        

lata_wartosc = []
surowce_energetyczne_wartosc = []

for i in range (1,len(i_e_w)):
    lata_wartosc.append (int(i_e_w [i][0]))
    surowce_energetyczne_wartosc.append(float(i_e_w [i][2]))

lata_wartosc=np.transpose(lata_wartosc)
surowce_energetyczne_wartosc=np.transpose(surowce_energetyczne_wartosc)

#saldo tonazu eksport - import 

lata_tonaz = []
surowce_energetyczne_tonaz = []

for i in range (1,len(i_e_t)):
    lata_tonaz.append (int(i_e_t [i][0]))
    surowce_energetyczne_tonaz.append(float(i_e_t [i][2]))

lata_tonaz=np.transpose(lata_tonaz)
surowce_energetyczne_tonaz=np.transpose(surowce_energetyczne_tonaz)




#WIZUALIZACJA - WYKRESY 

#saldo wartosci eksport - import    

fig = plt.figure()
ax = plt.subplot (111)
ax.bar(lata_wartosc,surowce_energetyczne_wartosc,width=1,color='b',edgecolor="r")

ylim(-60000,0)
xticks([2009,2010,2011,2012,2013,2014,2015,2016,2017,2018])
yticks([0,-5000,-10000,-15000,-20000,-25000,-30000,-35000,-40000,-45000,-50000,-55000,-60000])

title("SALDO WARTOŚCI EKSPORT - IMPORT SUROWCÓW MINERALNYCH W LATACH 2009 – 2018",fontsize=10) 
xlabel("Lata")  
ylabel("Surowce energetyczne")

plt.savefig("saldo wartosci i e.png", bbox_inches='tight')

#saldo tonaz eksport - import

fig = plt.figure()
ax = plt.subplot (111)
ax.bar(lata_tonaz,surowce_energetyczne_tonaz,width=1,color='r',edgecolor="b")

ylim(-40,0)
xticks([2009,2010,2011,2012,2013,2014,2015,2016,2017,2018])
yticks([0,-5,-10,-15,-20,-25,-30,-35,-40])

title("SALDO TONAŻU EKSPORT - IMPORT SUROWCÓW MINERALNYCH W LATACH 2009 – 2018",fontsize=10) 
xlabel("Lata")  
ylabel("Surowce energetyczne")

plt.savefig("saldo tonazu i e.png", bbox_inches='tight')




    