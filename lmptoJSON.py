import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json('output.json', lines=True)

xpoints = df['timestep'].values.tolist()
potential_energy = df['pe'].values.tolist()
kinetic_energy = df['ke'].values.tolist()
energy_total = df['etotal'].values.tolist()

plt.plot(xpoints, potential_energy)
plt.plot(xpoints, kinetic_energy)
plt.plot(xpoints, energy_total)

plt.legend(['Potential Energy','Kinetic Energy','Total Energy'])
plt.show()
