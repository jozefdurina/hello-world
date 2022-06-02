import matplotlib.pyplot as plt

x = [1,3,2,5]
y1 = [5,8,9,8]
y2 = [0,10,0,1]

fig, (ax1, ax2) = plt.subplots(2, sharex=True)
#plt . titul ( 'Histogram IQ' )
fig.suptitle('x verzus y1 a y2')
plt.plotfile('date', 'volume', 'adj_close')
plt.xlabel("os x")
plt.ylabel("os y" )
ax1.plot(x, y1)
#ax1.text(0,0, "prvy graf", verticalalignment='top')

ax2.plot(x, y2) 
#ax1.text(0,10, "druhy graf", verticalalignment='top')


plt.show()


# import matplotlib.pyplot as plt
# import matplotlib.transforms as mtransforms

# fig, axs = plt.subplot_mosaic([['a)', 'c)'], ['b)', 'c)'], ['d)', 'd)']],
#                               constrained_layout=True)

# for label, ax in axs.items():
#     # label physical distance in and down:
#     trans = mtransforms.ScaledTranslation(10/72, -5/72, fig.dpi_scale_trans)
#     ax.text(text(0.0, 1.0, label, transform=ax.transAxes + trans,
#             fontsize='medium', verticalalignment='top', fontfamily='serif',
#             bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))

# plt.show()