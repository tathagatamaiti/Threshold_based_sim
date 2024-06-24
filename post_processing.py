import matplotlib.pyplot as plt
import pandas as pd

# Read data from CSV files
pdus = pd.read_csv('pdus.csv')
upfs = pd.read_csv('upfs.csv')
active_pdus = pd.read_csv('active_pdus.csv')
active_upfs = pd.read_csv('active_upfs.csv')
free_slots = pd.read_csv('free_slots.csv')

# Plot PDU against simulation time
plt.figure(figsize=(10, 10))
plt.plot(pdus['Time'], pdus['PDUs'], color='blue')
plt.xlabel('Simulation Time in ms')
plt.ylabel('PDUs')
plt.title('PDUs vs Simulation Time')
plt.grid(True)
plt.savefig('pdu_vs_simulation_time.png')
plt.show()

# Plot UPF against simulation time
plt.figure(figsize=(10, 10))
plt.plot(upfs['Time'], upfs['UPFs'], color='green')
plt.xlabel('Simulation Time in ms')
plt.ylabel('UPFs')
plt.title('UPFs vs Simulation Time')
plt.grid(True)
plt.savefig('upf_vs_simulation_time.png')
plt.show()

# Plot active PDUs against simulation time
plt.figure(figsize=(10, 10))
plt.plot(active_pdus['Time'], active_pdus['Active PDUs'], color='red')
plt.xlabel('Simulation Time in ms')
plt.ylabel('Active PDUs')
plt.title('Active PDUs vs Simulation Time')
plt.grid(True)
plt.savefig('active_pdus_vs_simulation_time.png')
plt.show()

# Plot active UPFs against simulation time
plt.figure(figsize=(10, 10))
plt.plot(active_upfs['Time'], active_upfs['Active UPFs'], color='orange')
plt.xlabel('Simulation Time in ms')
plt.ylabel('Active UPFs')
plt.title('Active UPFs vs Simulation Time')
plt.grid(True)
plt.savefig('active_upfs_vs_simulation_time.png')
plt.show()

# Plot active UPFs against simulation time
plt.figure(figsize=(10, 10))
plt.plot(free_slots['Free Slots'], color='purple')
plt.xlabel('Simulation Time in ms')
plt.ylabel('Free Slots')
plt.title('Free Slots vs Simulation Time')
plt.grid(True)
plt.savefig('free_slots_vs_simulation_time.png')
plt.show()

# Calculate the duration for each interval where the number of active UPFs remains constant
active_pdus['Duration'] = active_pdus['Time'].diff().shift(-1)
active_upfs['Duration'] = active_upfs['Time'].diff().shift(-1)
free_slots['Duration'] = free_slots['Time'].diff().shift(-1)

# Group by 'Active UPFs' and sum the durations
duration_by_pdu = active_pdus.groupby('Active PDUs')['Duration'].sum()
duration_by_upf = active_upfs.groupby('Active UPFs')['Duration'].sum()
duration_by_free_slots = free_slots.groupby('Free Slots')['Duration'].sum()

# Normalize by the total time to get the PDF
total_time = duration_by_pdu.sum()
pdf_by_pdu = duration_by_pdu / total_time

total_time = duration_by_upf.sum()
pdf_by_upf = duration_by_upf / total_time

total_time = duration_by_free_slots.sum()
pdf_by_free_slots = duration_by_free_slots / total_time

# Convert to a DataFrame for better readability
pdf_pdu = pdf_by_pdu.reset_index().rename(columns={'Duration': 'PDF'})
pdf_upf = pdf_by_upf.reset_index().rename(columns={'Duration': 'PDF'})
pdf_free_slots = pdf_by_free_slots.reset_index().rename(columns={'Duration': 'PDF'})

# Plot the PDF of active PDUs
plt.figure(figsize=(10, 10))
plt.bar(pdf_pdu['Active PDUs'], pdf_pdu['PDF'], edgecolor='k', alpha=0.7)
plt.xlabel('Active PDUs')
plt.ylabel('PDF')
plt.title('Probability Density Function of Active PDUs')
plt.xticks(pdf_pdu['Active PDUs'])
plt.savefig('active_pdus_pdf.png')
plt.show()


# Plot the PDF of active UPFs
plt.figure(figsize=(10, 10))
plt.bar(pdf_upf['Active UPFs'], pdf_upf['PDF'], edgecolor='k', alpha=0.7)
plt.xlabel('Active UPFs')
plt.ylabel('PDF')
plt.title('Probability Density Function of Active UPFs')
plt.xticks(pdf_upf['Active UPFs'])
plt.savefig('active_upfs_pdf.png')
plt.show()

# Plot the PDF of Free Slots
plt.figure(figsize=(10, 10))
plt.bar(pdf_free_slots['Free Slots'], pdf_free_slots['PDF'], edgecolor='k', alpha=0.7)
plt.xlabel('Free Slots')
plt.ylabel('PDF')
plt.title('Probability Density Function of Free Slots')
plt.xticks(pdf_free_slots['Free Slots'])
plt.savefig('free_slots_pdf.png')
plt.show()
