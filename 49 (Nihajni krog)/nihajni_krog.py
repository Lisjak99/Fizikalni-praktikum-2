import numpy as np

#praznjenje

U_0 = 12.00
R_1 = 38000
R = 200
C = 0.22 * 10**(-6)
L = 1.227
tau = R_1 * C


beta = 0.5 * (R/L)
w_0 = np.sqrt(1/(L*C))
w = np.sqrt((w_0)**2 - (beta)**2)

I_o = U_0/R
U_o = I_o * R

import matplotlib.pyplot as plt


x = np.linspace(0, 0.08, 1000)

#y = U_0 * np.exp(-x/tau)

#polnjenje
#y = U_0*(1 - np.exp(-x/tau))

#NIHAJNI KROG

y = I_o * R * np.exp(-beta*x) * ( ((beta/w)-(1/(w * R * L))) * np.sin(w*x) + np.cos(w*x) )
y_p = -(I_o/(w_0 * C) * np.exp(-beta*x)) * np.sin(w_0 * x)

fig, (ax1, ax2) = plt.subplots(2, sharex = True)
ax1.set_title("Primerjava med približkom in točno vrednostjo nihajnega kroga")

ax1.plot(x, y)
ax2.plot(x, y_p)

plt.xlabel("t[ms]")
plt.ylabel("U[V]")

#plt.plot(x,y, 'b.')
plt.show()
print(tau)



