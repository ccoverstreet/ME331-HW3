# ME 331: HW 3
# Cale Overstreet
# February 11, 2020

import matplotlib.pyplot as plt
import numpy as np

x_data = []
density  = []
pressure = []
temperature = []
for i in range(0, 25000):
    h = i / 1000
    x_data.append(h)
    temp_density = 1.225 * np.e ** (-1 * i / 7249)
    density.append(temp_density)
    temp_pressure = (9.8 * 1.225 * 7249 * np.e ** (-1 * i / 7249) + 101325)
    pressure.append(temp_pressure / 1000)
    temperature.append((temp_pressure / (287 * temp_density)))


plt.plot(x_data, density)
plt.title("Density behavior from 0-25 km")
plt.xlabel("Altitude (km)")
plt.ylabel("Density (kg/$m^3$)")
plt.show()

plt.plot(x_data, pressure)
plt.title("Pressure behavior from 0-25 km")
plt.xlabel("Altitude (km)")
plt.ylabel("Pressure (kPa)")
plt.show()

plt.plot(x_data, temperature)
plt.title("Temperature behavior from 0-25 km")
plt.xlabel("Altitude (km)")
plt.ylabel("Temperature (K)")
plt.show()
