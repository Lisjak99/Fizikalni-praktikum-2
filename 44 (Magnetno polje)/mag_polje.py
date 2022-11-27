import numpy as np 
import matplotlib.pyplot as plt
from scipy import stats


# DOKAZ SORAZMERNOSTI "TOK - SILA" -----------------------

# Podatki
meritve_vse = []

vsi = open("/Users/saralisjakt/Desktop/mag_polje_sila_1.txt", "r")
for line in vsi:
    line_c = line.rstrip().split(" ")
    meritve_vse.append( ((float(line_c[0]), float(line_c[1]))) )

vsi = open("/Users/saralisjakt/Desktop/mag_polje_sila_2.txt", "r")
for line in vsi:
    line_c = line.rstrip().split(" ")
    meritve_vse.append( ((float(line_c[0]), float(line_c[1]))) )

# Skpen graf
mer = np.sort(meritve_vse)

fig = plt.figure()
ax = fig.gca()
ax.set(title = "Odvisnost mase od toka", xlabel = "I[mA]", ylabel = "m[g]")

ax.scatter(mer[:,1], mer[:,0], c="rebeccapurple")
m3, b3 = np.polyfit(mer[:,1], mer[:,0], 1)
ax.plot(np.array(mer[:,1]), m3 * np.array(mer[:,1]) + b3, alpha = 0.5, label = r'$\alpha$' " = {}".format(m3))


plt.show()

# Linearna regresija
res_1 = stats.linregress(np.array(mer[:,1]), np.array(mer[:,0]))
delta_1 = res_1.stderr / res_1.slope

# MAG. POLJE IN MAG. PRETOK ------------------------------------------

# Podatki
S_mag = 0.4 * 2.0 * 10**(-4)  # [m**2]
delta_S_mag = 0.235
napaka_S_mag = S_mag * delta_S_mag

l = 0.02 # [m]
delta_l = 0.05
napaka_l = l * delta_l

g = 9.81
delta_g = 0.01

alfa = m3 # masa/tok
delta_alfa = delta_1

# Rezultat
B = (alfa * g) / l
delta_B = delta_alfa + delta_g + delta_l
napaka_B = B * delta_B

Pretok = B * S_mag
delta_pretok = delta_B + delta_S_mag
napaka_pretok = Pretok * delta_pretok


print(B, napaka_B)

