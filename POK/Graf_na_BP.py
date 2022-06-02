
import matplotlib.pyplot as plt

x=[10,20,30,40,50]
y1=[1,2,3,4,5] 
y2=[1.1e-3,2.2e-3,1.5e-3,4e-3,5e-3]
# y3=[20,40,60,80,100]
# y4=[5,10,15,20,25]
# y5=[15,20,25,30,35]
# y6=[25,30,35,40,45]
fig, host = plt.subplots()
fig.subplots_adjust(left=0.75)   

par1 = host.twinx()

par1.spines["left"].set_position(("axes", 1.2))

p1, = host.plot(x, y1, "b-", label="y1")
p2, = par1.plot(x, y2, "r-", label="y2")




plt.title('Typstoziara_Druhanalyzy_rozsahod_rozsahdo_krokrozsahu')
plt.xlabel('Parameter (m)')
plt.ylabel('Z(ohm)')

plt.legend()
plt.tight_layout()
plt.show()