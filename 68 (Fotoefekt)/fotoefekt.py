import numpy as np 
import matplotlib.pyplot as plt
from scipy import stats

#----------------------------------------------------
# odvisnost katodnega toka od zaporne napetosti za vsak barvni filter

# podatki
lambda_1 = 365 * 10**(-9) #m
lambda_2 = 405 * 10**(-9) #m
lambda_3 = 436 * 10**(-9) #m
lambda_4 = 546 * 10**(-9) #m

# lambda 1_________________________________________________
nap_1 = []  # V
tok_1 = []    # 10**(-13) A

vsi = open("/Users/saralisjakt/Desktop/lambda_365.txt", "r")
for line in vsi:
    line_c = line.rstrip().split(" ")
    nap_1.append(float(line_c[0]))
    tok_1.append(float(line_c[1]) * 10**(-13))

vrednost_zamika1 = nap_1[0]
napetost_1 = np.array(nap_1) - abs(vrednost_zamika1)

# lambda 2___________________________________________________
nap_2 = []  # V
tok_2 = []    # 10**(-13) A

vsi2 = open("/Users/saralisjakt/Desktop/lambda_405.txt", "r")
for line in vsi2:
    line_c = line.rstrip().split(" ")
    nap_2.append(float(line_c[0]))
    tok_2.append(float(line_c[1]) * 10**(-13))

vrednost_zamika2 = nap_2[0]
napetost_2 = np.array(nap_2) - abs(vrednost_zamika2)

# lambda 3___________________________________________________
nap_3 = []  # V
tok_3 = []    # 10**(-13) A

vsi3 = open("/Users/saralisjakt/Desktop/lambda_436.txt", "r")
for line in vsi3:
    line_c = line.rstrip().split(" ")
    nap_3.append(float(line_c[0]))
    tok_3.append(float(line_c[1]) * 10**(-13))

vrednost_zamika3 = nap_3[0]
napetost_3 = np.array(nap_3) - abs(vrednost_zamika3)

# lambda 4__________________________________________________
nap_4 = []  # V
tok_4 = []    # 10**(-13) A

vsi4 = open("/Users/saralisjakt/Desktop/lambda_546.txt", "r")
for line in vsi4:
    line_c = line.rstrip().split(" ")
    nap_4.append(float(line_c[0]))
    tok_4.append(float(line_c[1]) * 10**(-13))


# zamik grafa
vrednost_zamika4 = nap_4[1]
napetost_4 = np.array(nap_4) - abs(vrednost_zamika4)


# lambda 5__________________________________________________
nap_5 = []  # V
tok_5 = []    # 10**(-13) A

vsi5 = open("/Users/saralisjakt/Desktop/lambda_577.txt", "r")
for line in vsi5:
    line_c = line.rstrip().split(" ")
    nap_5.append(float(line_c[0]))
    tok_5.append(float(line_c[1]) * 10**(-13))


# zamik grafa
vrednost_zamika5 = nap_5[1]
napetost_5 = np.array(nap_5) - abs(vrednost_zamika5)

# GRAFI
#graf1------------------------------------------
fig1 = plt.figure()
ax1 = fig1.gca()
ax1.set(title = "tok - napetost, lambda = 365nm", xlabel = "U_m[V]", ylabel = "I[10**(-13) A]")

ax1.scatter(napetost_1, tok_1, c="rebeccapurple", label = "365")
ax1.plot([napetost_1[0],napetost_1[-1]],[0,0] , "gray")

#prilagoditvena krivulja
u = np.array(napetost_1)

m, b = np.polyfit(u, tok_1, 1)
plt.plot(u, m * u + b)

res = stats.linregress(u, tok_1)
delta_1 = res.stderr / res.slope

#graf2-------------------------------------------
fig2 = plt.figure()
ax2 = fig2.gca()
ax2.set(title = "tok - napetost, lambda = 405nm", xlabel = "U_m[V]", ylabel = "I[10**(-13) A]")

ax2.scatter(napetost_2, tok_2, c="darkviolet", label = "405")
ax2.plot([napetost_2[0],napetost_2[-1]],[0,0] , "gray")


#prilagoditvena krivulja
u2 = np.array(napetost_2)

m2, b2 = np.polyfit(u2, tok_2, 1)
plt.plot(u2, m2 * u2 + b2)

res2 = stats.linregress(u2, tok_2)
delta_2 = res2.stderr / res2.slope


#graf3----------------------------------------------
fig3 = plt.figure()
ax3 = fig3.gca()
ax3.set(title = "tok - napetost, lambda = 436nm", xlabel = "U_m[V]", ylabel = "I[10**(-13) A]")

ax3.scatter(napetost_3, tok_3, c="darkblue", label = "436")
ax3.plot([napetost_3[0],napetost_3[-1]],[0,0] , "gray")

#prilagoditvena krivulja
u3 = np.array(napetost_3)

m3, b3 = np.polyfit(u3, tok_3, 1)
plt.plot(u3, m3 * u3 + b3)

res = stats.linregress(u3, tok_3)
delta_3 = res.stderr / res.slope


#graf4---------------------------------------------
fig4 = plt.figure()
ax4 = fig4.gca()
ax4.set(title = "tok - napetost, lambda = 546nm", xlabel = "U_m[V]", ylabel = "I[10**(-13) A]")

ax4.scatter(napetost_4, tok_4, c="yellowgreen", label = "546")
ax4.plot([napetost_4[0],napetost_4[-1]],[0,0] , "gray")

#prilagoditvena krivulja
u4 = np.array(napetost_4)

m4, b4 = np.polyfit(u4, tok_4, 1)
plt.plot(u4, m4 * u4 + b4)

res = stats.linregress(u4, tok_4)
delta_4 = res.stderr / res.slope

#graf5----------------------------------------------
fig5 = plt.figure()
ax5 = fig5.gca()
ax5.set(title = "tok - napetost, lambda = 577nm", xlabel = "U_m[V]", ylabel = "I[10**(-13) A]")

ax5.scatter(napetost_5, tok_5, c="yellow", label = "577")
ax5.plot([napetost_5[0],napetost_5[-1]],[0,0] , "gray")

#prilagoditvena krivulja
u5 = np.array(napetost_5)

m5, b5 = np.polyfit(u5, tok_5, 1)
plt.plot(u5, m5 * u5 + b5)

res = stats.linregress(u5, tok_5)
delta_5 = res.stderr / res.slope



#-----------------------------------------------------
# Mejne zaporne napetosti (ko doseze tok vrednost 0)
mejne_zap_napetosti = [2.6, 2.2, 2.1, 1.65, 1.21] # odčitane iz grafa, pri presečišču premic
max_Wk = np.array(mejne_zap_napetosti) * 10**(-19)

#podatki
c = 3 * 10**8
#frekvenca = (c / 577* 10**(-9)) * 10**(-12)
frekvence = np.array([821.9, 740.7, 688.0, 549.5, 518.9]) * 10**(12)

#graf energije od frekvence
fig5 = plt.figure()
ax5 = fig5.gca()
ax5.set(title = "energija od frekvence", xlabel = "ni[Hz]", ylabel = "W[eV]")

ax5.scatter(frekvence, max_Wk, c="black", label = "A")



#prilagoditvena krivulja
h, b5 = np.polyfit(frekvence, max_Wk, 1)
plt.plot(frekvence, h * frekvence + b5)


N = np.array([i for i in range(10)]) * 10**(14)
plt.plot(N, h * N + b5, "--", c="gray")
plt.ylim([-1 * 10**(-19), 3.5 * 10**(-19)])
plt.xlim([0 * 10**(12), 900 * 10**(12)])


res_h = stats.linregress(frekvence, mejne_zap_napetosti)
delta_h = res_h.stderr / res_h.slope

napaka_h = h * delta_h
print(napaka_h)

plt.show()