import numpy as np 
import matplotlib.pyplot as plt
from scipy import stats

#Podatki
C_0 = 580 * 10**(-12) #F
L_0 = 8235
ni = 600000

vsi_0 = open("/Users/saralisjakt/Desktop/0ohm.txt", "r")


# Umeritev
enote = []
kapa = []

vsi = open("/Users/saralisjakt/Desktop/umeritev.txt", "r")
for line in vsi:
    line_c = line.rstrip().split(" ")
    enote.append((float(line_c[0])))
    kapa.append((float(line_c[1])))

# Graf umeritve
"""fig1 = plt.figure()
ax1 = fig1.gca()
ax1.set(title = "Umeritvena Krivulja", xlabel = "enote razdelka", ylabel = "C[pF]")

ax1.scatter(enote, kapa, c="rebeccapurple")

res_1 = stats.linregress(np.array(enote), np.array(kapa))
delta_1 = res_1.stderr / res_1.slope
"""
# Resonančne krivulje
kapaciteta_0 = []
napetostL_0 = []
napetostD_0 = []

napetostL_10 = []
napetostD_10 = []

napetostL_20 = []

for line in vsi_0:
    line_c = line.rstrip().split(" ")
    kapaciteta_0.append((float(line_c[1])))
    napetostL_0.append((float(line_c[2])))
    napetostD_0.append((float(line_c[3])))
    napetostL_10.append((float(line_c[4])))
    napetostD_10.append((float(line_c[5])))
    napetostL_20.append((float(line_c[6])))


U_0_L = napetostL_0[0]
U_0_D = napetostD_0[0]

rel_0_L = np.array(napetostL_0)/U_0_L
rel_0_D = np.array(napetostD_0)/U_0_D
rel_10_L = np.array(napetostL_10)/napetostL_10[0]
rel_10_D = np.array(napetostD_10)/napetostD_10[0]
rel_20_L = np.array(napetostL_20)/napetostL_20[0]


# Graf
fig2 = plt.figure()
ax2 = fig2.gca()
ax2.set(title = "Resonančna krivulja Krivulja - PRIMERJAVA", xlabel = "kapaciteta[pF]", ylabel = "U/U_i")

ax2.scatter(kapaciteta_0, rel_0_L, c="rebeccapurple", label = "0 OHM")
ax2.scatter(kapaciteta_0, rel_10_L, c="limegreen", label = "10 OHM")
ax2.scatter(kapaciteta_0, rel_20_L, c="blue", label = "20 OHM")

handles, labels = ax2.get_legend_handles_labels()
ax2.legend(handles, labels, fontsize = 10)

plt.show()


