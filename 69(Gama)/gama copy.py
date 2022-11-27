import numpy as np 
import math as m
import matplotlib.pyplot as plt
from scipy import stats


# Podatki
fi_0 = 2.12
x = np.sqrt(((0.8)**2+(17.8)**2+(18.2)**2+(0.2)**2+(2.2)**2+(1.8)**2)/30)
w = np.sqrt(((1.8)**2+(0.2)**2+(2.8)**2+(2.8)**2+(10.2)**2+(2.8)**2)/30)
n = np.sqrt(((3.7)**2+(14.3)**2+(1.3)**2+(7.3)**2+(3.7)**2+(15.7)**2)/30)

v = np.sqrt(((569)**2+(237)**2+(143)**2+(232)**2+(633)**2+(172)**2+(881)**2)/42)
y = np.sqrt(((514)**2+(392)**2+(302)**2+(215)**2+(702)**2+(211)**2+(16)**2+(83)**2)/56)
p = np.sqrt(((419)**2+(14)**2+(276)**2+(102)**2+(8)**2+(62)**2)/42)

print(v,y,p)

toki = [1.70,1.63,1.38,1.34]
debeline = [1.62, 3.77, 5.43, 7.03]
rez = []
for i in range(len(toki)):
    rez.append(np.log(fi_0/toki[i]))

fig1 = plt.figure()
ax1 = fig1.gca()
ax1.scatter(debeline[:], rez[:], c="rebeccapurple")
ax1.set(title = "lineariziran graf", xlabel = "debelina[mm]", ylabel = "log(fi_0/fi)")


m1, b1 = np.polyfit(debeline[:], rez[:], 1)
ax1.plot(np.array(debeline), m1 * np.array(debeline) + b1, alpha = 0.5, label = "koeficient absorbcije '$\mu$' " )

res_1 = stats.linregress(np.array(debeline), np.array(rez))
delta_1 = res_1.stderr / res_1.slope


handles, labels = ax1.get_legend_handles_labels()
ax1.legend(handles, labels, fontsize = 10)


print(res_1,delta_1)
"""N_p = 123
x = [i for i in range(11)]
W = []
for i in range(11):
    W.append((N_p**i)/m.factorial(i) * np.exp(-N_p))

"""
"""# Grafi

ax1.set(title = "diagram napetost**2 od mase", xlabel = "m[kg]", ylabel = "U**2[V**2]")


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
print(d)"""