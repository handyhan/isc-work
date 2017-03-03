import matplotlib.pyplot as plt
import numpy as np
fig, ax1 = plt.subplots()

time = np.array(range(7))
co_conc = np.array([250,265,272,260,300,320,389])

ax1.plot(time,co_conc, label = 'CO\_2 Concentration (ppm)', color = 'r')

ax1.set_ylabel('[CO2]')

ax2=ax1.twinx()
temp = np.array([14.1,15.5,16.3,18.1,17.3,19.1,20.2])
ax2.plot(time,temp, label = 'Temperature',color = 'b')
ax2.set_ylabel('Temp (degC)')

plt.show()
