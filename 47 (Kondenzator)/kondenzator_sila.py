import numpy as np 
import matplotlib.pyplot as plt
from scipy import stats


# Podatki
g = 9.81
delta_g = 0.01

r = 9.5 * 0.01 
delta_r = 0.01

S = np.pi * r**2
delta_S = 0.02
napaka_S = S * delta_S

d = 0.51 * 0.01
delta_d = 0.02
napaka_d = d * delta_d

masa = []
napetost_1 = []
napetost_2 = []
napetost_3 = []

vsi = open("/Users/saralisjakt/Desktop/sila_kondenzator_1.txt", "r")
for line in vsi:
    line_c = line.rstrip().split(" ")
    masa.append(float(line_c[0]) / 1000000)
    napetost_1.append(float(line_c[1]) * 1000)
    napetost_2.append(float(line_c[2]) * 1000)
    napetost_3.append(float(line_c[3]) * 1000)


napetost_pov_sqrt = ((np.array(napetost_1) + np.array(napetost_2) + np.array(napetost_3)) / 3 )**2

# Grafi
fig1 = plt.figure()
ax1 = fig1.gca()
ax1.set(title = "diagram napetost**2 od mase", xlabel = "m[kg]", ylabel = "U**2[V**2]")

ax1.scatter(masa, napetost_pov_sqrt, c="rebeccapurple")
m1, b1 = np.polyfit(masa, napetost_pov_sqrt, 1)
ax1.plot(np.array(masa), m1 * np.array(masa) + b1, alpha = 0.5, label = r'$\alpha$' " = {}".format(m1))

res_1 = stats.linregress(np.array(masa), np.array(napetost_pov_sqrt))
delta_1 = res_1.stderr / res_1.slope

handles, labels = ax1.get_legend_handles_labels()
ax1.legend(handles, labels, fontsize = 10)


# Izračuni
konst = (2 * g * d**2) / S 
epsilon = (1 / m1) * konst
delta_epsilon = delta_1 + 2 * delta_d + delta_g + delta_S
napaka_epsilon = epsilon * delta_epsilon


c = 2.998 * 10**8
permeabilnost = 4 * np.pi * 10**(-7)
epsilon_primerjava = (c**2 * permeabilnost)**(-1)

print(epsilon, epsilon_primerjava)
plt.show() 


# Dodatek ----------------------------------------------------------------

d = np.sqrt( (epsilon_primerjava * S * m1) / (2 * g))
print(d)