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
plt.savefig('pdu_vs_simulation_time_case1.png')
plt.show()

# Plot UPF against simulation time
plt.figure(figsize=(10, 10))
plt.plot(upfs['UPFs'], color='green')
plt.xlabel('Simulation Time in ms')
plt.ylabel('UPFs')
plt.title('UPFs vs Simulation Time')
plt.grid(True)
plt.savefig('upf_vs_simulation_time_case1.png')
plt.show()

# Plot active PDUs against simulation time
plt.figure(figsize=(10, 10))
plt.plot(active_pdus['Active PDUs'], color='red')
plt.xlabel('Simulation Time in ms')
plt.ylabel('Active PDUs')
plt.title('Active PDUs vs Simulation Time')
plt.grid(True)
plt.savefig('active_pdus_vs_simulation_time_case1.png')
plt.show()

# Plot active UPFs against simulation time
plt.figure(figsize=(10, 10))
plt.plot(active_upfs['Active UPFs'], color='orange')
plt.xlabel('Simulation Time in ms')
plt.ylabel('Active UPFs')
plt.title('Active UPFs vs Simulation Time')
plt.grid(True)
plt.savefig('active_upfs_vs_simulation_time_case1.png')
plt.show()

active_pdus['Time'] = pd.to_datetime(active_pdus['Time'])
active_upfs['Time'] = pd.to_datetime(active_upfs['Time'])

active_pdus['Next_Time'] = active_pdus['Time'].shift(-1)
active_pdus['Duration'] = ((active_pdus['Next_Time'] - active_pdus['Time']).fillna(pd.Timedelta(seconds=0)).
                           dt.total_seconds())

active_upfs['Next_Time'] = active_upfs['Time'].shift(-1)
active_upfs['Duration'] = ((active_upfs['Next_Time'] - active_upfs['Time']).fillna(pd.Timedelta(seconds=0)).
                           dt.total_seconds())

duration_data_pdus = active_pdus[active_pdus['Active PDUs'] != active_pdus['Active PDUs'].shift(-1)]
duration_data_upfs = active_upfs[active_upfs['Active UPFs'] != active_upfs['Active UPFs'].shift(-1)]

duration_by_pdu = duration_data_pdus.groupby('Active PDUs')['Duration'].sum()
duration_by_upf = duration_data_upfs.groupby('Active UPFs')['Duration'].sum()

# Plot the total duration each 'Active UPFs' value is observed
plt.figure(figsize=(10, 10))
duration_by_pdu.plot(kind='bar', color='blue', edgecolor='black')
plt.xlabel('Active PDUs')
plt.ylabel('Total Time Observed (seconds)')
plt.title('Total Time Each Active PDU is Observed')
plt.grid(True)
plt.savefig('active_pdu_histogram_case1.png')
plt.show()

# Plot the total duration each 'Active UPFs' value is observed
plt.figure(figsize=(10, 10))
duration_by_upf.plot(kind='bar', color='green', edgecolor='black')
plt.xlabel('Active UPFs')
plt.ylabel('Total Time Observed (seconds)')
plt.title('Total Time Each Active UPF is Observed')
plt.grid(True)
plt.savefig('active_upf_histogram_case1.png')
plt.show()
