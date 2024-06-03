import matplotlib.pyplot as plt
import pandas as pd

# Read data from CSV files
pdus = pd.read_csv('pdus.csv')
upfs = pd.read_csv('upfs.csv')
active_pdus = pd.read_csv('active_pdus.csv')
active_upfs = pd.read_csv('active_upfs.csv')

# Plot PDU against simulation time
plt.figure(figsize=(10, 10))
plt.plot(pdus['PDUs'], color='blue')
plt.xlabel('Simulation Time in ms')
plt.ylabel('PDUs')
plt.title('PDUs vs Simulation Time')
plt.grid(True)
plt.savefig('pdu_vs_simulation_time.png')
plt.show()

# Plot UPF against simulation time
plt.figure(figsize=(10, 10))
plt.plot(upfs['UPFs'], color='green')
plt.xlabel('Simulation Time in ms')
plt.ylabel('UPFs')
plt.title('UPFs vs Simulation Time')
plt.grid(True)
plt.savefig('upf_vs_simulation_time.png')
plt.show()

# Plot active PDUs against simulation time
plt.figure(figsize=(10, 10))
plt.plot(active_pdus['Active PDUs'], color='red')
plt.xlabel('Simulation Time in ms')
plt.ylabel('Active PDUs')
plt.title('Active PDUs vs Simulation Time')
plt.grid(True)
plt.savefig('active_pdus_vs_simulation_time.png')
plt.show()

# Plot active UPFs against simulation time
plt.figure(figsize=(10, 10))
plt.plot(active_upfs['Active UPFs'], color='orange')
plt.xlabel('Simulation Time in ms')
plt.ylabel('Active UPFs')
plt.title('Active UPFs vs Simulation Time')
plt.grid(True)
plt.savefig('active_upfs_vs_simulation_time.png')
plt.show()

# Create histograms for active PDUs
plt.figure(figsize=(10, 10))
plt.hist(active_pdus['Active PDUs'], bins=20, edgecolor='black')
plt.xlabel('Number of Active PDUs')
plt.ylabel('Frequency')
plt.title('Frequency of Active PDUs')
plt.savefig('active_pdus_hist.png')
plt.show()

# Create histograms for active UPFs
plt.figure(figsize=(10, 10))
plt.hist(active_upfs['Active UPFs'], bins=20, edgecolor='black')
plt.xlabel('Number of Active UPFs')
plt.ylabel('Frequency')
plt.title('Frequency of Active UPFs')
plt.savefig('active_upfs_hist.png')
plt.show()
