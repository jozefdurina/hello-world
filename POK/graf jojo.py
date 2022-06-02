import matplotlib.pyplot as plt


fig, ax = plt.subplots()         #deklaruje že fig a ax su subplots
fig.subplots_adjust(right=0.75)  # posun pravej osi y prvej plochy do 3/4 okna

twin1 = ax.twinx()
twin2 = ax.twinx()


# Offset the right spine of twin2.  The ticks and label have already been
# placed on the right by twinx above.
twin2.spines.right.set_position(("axes", 1.2))  # twin2 pravu os y posuva na poziciu 1.2 o 1.0 osi x - 1.4 už nie je v okne vidieť

p1, = ax.plot([0, 1, 2], [0, 1, 2], "b-", label="a")   # , je dolezita neviem preco
p11, = ax.plot([0, 1, 2], [0, 3, 5], "b--", label="b")   
p2, = twin1.plot([0, 1, 2], [0, 3, 2], "r-", label="c")
p21, = twin1.plot([0, 1, 2], [0, 2, 1], "r--", label="d")
p3, = twin2.plot([0, 1, 3], [50, 30, 15], "g-", label="e")
p31, = twin2.plot([0, 1, 3], [40, 20, 35], "g--", label="f")

ax.set_xlim(0,5 )
ax.set_ylim(0, 5)
twin1.set_ylim(0, 4)
twin2.set_ylim(1, 65)

ax.set_xlabel("Distance")
ax.set_ylabel("Density")
twin1.set_ylabel("Temperature")
twin2.set_ylabel("Velocity")

ax.yaxis.label.set_color(p1.get_color())
twin1.yaxis.label.set_color(p2.get_color())
twin2.yaxis.label.set_color(p3.get_color())


tkw = dict(size=4, width=1.5)                              #okno
ax.tick_params(axis='y', colors=p1.get_color(), **tkw)
twin1.tick_params(axis='y', colors=p2.get_color(), **tkw)
twin2.tick_params(axis='y', colors=p3.get_color(), **tkw)
ax.tick_params(axis='x', **tkw)

ax.legend(handles=[p1,p11,p2,p21,p3,p31]) 
   

plt.show()