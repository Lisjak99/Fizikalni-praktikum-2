import numpy as np 
import matplotlib.pyplot as plt
from scipy import stats

#----------------------------------------------------------------
#upornik 1

#podatki 
l = 1 # +- 0.01 m

levi_a = []
desni_a = []
upor_0 = []

vsi = open("/Users/saralisjakt/Desktop/wheatsonov_most_1.txt", "r")
for line in vsi:
    line_c = line.rstrip().split(" ")
    upor_0.append(float(line_c[0]))
    levi_a.append(float(line_c[1]) * 0.01)
    desni_a.append(float(line_c[2]) * 0.01)


# izracun razmerij razdalj za levo in desno stran meritev
R_x_l = []

for i in range(len(upor_0)):
    R_x_l.append( (l - levi_a[i])/levi_a[i] )


R_x_d = []

for i in range(len(upor_0)):
    R_x_d.append(desni_a[i] /(l - desni_a[i]))


#graficni prikaz
fig = plt.figure()
ax = fig.gca()
ax.set(title = "Porazdelitev levih in desnih meritev ", xlabel = "R_0", ylabel = "l-a/a")

ax.scatter(upor_0, R_x_d, c="C2", label = "Desne meritve (obrnjene)")
ax.scatter(upor_0, R_x_l, c="C4", label = "Leve meritve (začetne)")


handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, fontsize = 15)


#aritmetična sredina
R = (np.array(R_x_l) + np.array(R_x_d)) / 2

fig2 = plt.figure()
ax2 = fig2.gca()
ax2.set(title = "Aritmetična sredina", xlabel = "R_0", ylabel = "l-a/a")

ax2.scatter(upor_0, R, c="C3")


#prilagoditvena krivulja
u = np.array(upor_0)

m, b = np.polyfit(u, R, 1)
plt.plot(u, m * u + b)


# odstopanje meritev od prilagoditvene krivulje
res = stats.linregress(u, R)
delta_R1 = res.stderr / res.slope

R1 = 1/m # +- R1 * napaka
napaka_upor1 = R1 * delta_R1


#---------------------------------------------------------------
# uporna žica

#podatki 
l_z = 1.05 # +- 0.01
d_z = 0.51 * 0.001  # +- 0.01 * 0.001
S_z = (d_z/2)**2 * np.pi

delta_S = (0.01/0.51)**2  #napaka ploscine


levizica_a = []
desnizica_a = []
uzica_0 = []

vsi = open("/Users/saralisjakt/Desktop/wheatsonov_most_2.txt", "r")

for line in vsi:
    line_c = line.rstrip().split(" ")
    uzica_0.append(float(line_c[0]))
    levizica_a.append(float(line_c[1]) * 0.01)
    desnizica_a.append(float(line_c[2]) * 0.01)


# izracun razmerij razdalj za levo in desno stran meritev
Rz_x_l = []

for i in range(len(uzica_0)):
    Rz_x_l.append(levizica_a[i]/(l - levizica_a[i]))

Rz_x_d = []

for i in range(len(uzica_0)):
    Rz_x_d.append((l - desnizica_a[i]) /desnizica_a[i])


#graficni prikaz
fig3 = plt.figure()
ax3 = fig3.gca()
ax3.set(title = "Porazdelitev levih in desnih meritev (zica)", xlabel = "R_0", ylabel = "l-a/a")

ax3.scatter(uzica_0, Rz_x_d, c="C2", label = "Desne meritve (obrnjene)")
ax3.scatter(uzica_0, Rz_x_l, c="C4", label = "Leve meritve (začetne)")

handles, labels = ax3.get_legend_handles_labels()
ax3.legend(handles, labels, fontsize = 15)


#aritmetična sredina
Rz = (np.array(Rz_x_l) + np.array(Rz_x_d)) / 2

fig4 = plt.figure()
ax4 = fig4.gca()
ax4.set(title = "Aritmetična sredina (zica)", xlabel = "R_0", ylabel = "l-a/a")

ax4.scatter(uzica_0, Rz, c="C3")


#prilagoditvena krivulja
uz = np.array(uzica_0)

j, r = np.polyfit(uz, Rz, 1)
plt.plot(uz, j * uz + r)


# odstopanje meritev od prilagoditvene krivulje
res_z = stats.linregress(uz, Rz)
delta_z = res_z.stderr / res_z.slope

R2 = 1/r # +- R2 * napaka
napaka_upor_zica = R2 * delta_z


#SPECIFIČNA UPORNOST
zeta = (S_z * R2) / l_z

zeta_druge_enote = zeta * 10**(6)

# napaka izračuna 
delta_zeta = (0.01/1.05) + (delta_S + delta_z)
napaka_zeta = delta_zeta * zeta

napaka_zeta_druge_enote = napaka_zeta * 10**(6)


#--------------------------------------------------------------
#KONČNI REZULTAT

print("upornik 1: " f"{R1}[ohm] +- {napaka_upor1}[ohm]")
print("upornik 2(zica): " f"{R2}[ohm] +- {napaka_upor_zica}[ohm]")
print("specifična upornost: " f"{zeta_druge_enote}[ohm*m] +- {napaka_zeta_druge_enote}[ohm*m]")

