import matplotlib.pyplot as plt
import argparse
import numpy as np
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description='Post-process simulation results')
    parser.add_argument('--input-files', type=str, nargs=7, required=True, help='Input CSV files to process')
    args = parser.parse_args()

    process_results(args.input_files)


def process_results(input_files):
    # Read data from CSV files
    pdus = pd.read_csv(input_files[0])
    upfs = pd.read_csv(input_files[1])
    active_pdus = pd.read_csv(input_files[2])
    busy_upfs = pd.read_csv(input_files[3])
    idle_upfs = pd.read_csv(input_files[4])
    free_slots = pd.read_csv(input_files[5])
    rejected_sessions = pd.read_csv(input_files[6])

    # Plot PDU against simulation time
    plt.figure(figsize=(20, 10))
    plt.plot(pdus['Time'], pdus['PDUs'], color='blue')
    plt.xlabel('Simulation Time in ms')
    plt.ylabel('PDUs')
    plt.title('PDUs vs Simulation Time')
    plt.grid(True)
    plt.savefig('../Results/pdu_vs_simulation_time.png')
    plt.show()

    # Plot UPF against simulation time
    plt.figure(figsize=(20, 10))
    plt.plot(upfs['Time'], upfs['UPFs'], color='green')
    plt.xlabel('Simulation Time in ms')
    plt.ylabel('UPFs')
    plt.title('UPFs vs Simulation Time')
    plt.grid(True)
    plt.savefig('../Results/upf_vs_simulation_time.png')
    plt.show()

    # Plot active PDUs against simulation time
    plt.figure(figsize=(20, 10))
    plt.plot(active_pdus['Time'], active_pdus['Active PDUs'], color='red')
    plt.xlabel('Simulation Time in ms')
    plt.ylabel('Active PDUs')
    plt.title('Active PDUs vs Simulation Time')
    plt.grid(True)
    plt.savefig('../Results/active_pdus_vs_simulation_time.png')
    plt.show()

    # Plot busy UPFs against simulation time
    plt.figure(figsize=(20, 10))
    plt.plot(busy_upfs['Time'], busy_upfs['Busy UPFs'], color='orange')
    plt.xlabel('Simulation Time in ms')
    plt.ylabel('Busy UPFs')
    plt.title('Busy UPFs vs Simulation Time')
    plt.grid(True)
    plt.savefig('../Results/busy_upfs_vs_simulation_time.png')
    plt.show()

    # Plot idle UPFs against simulation time
    plt.figure(figsize=(20, 10))
    plt.plot(idle_upfs['Time'], idle_upfs['Idle UPFs'], color='orange')
    plt.xlabel('Simulation Time in ms')
    plt.ylabel('Idle UPFs')
    plt.title('Idle UPFs vs Simulation Time')
    plt.grid(True)
    plt.savefig('../Results/idle_upfs_vs_simulation_time.png')
    plt.show()

    # Plot free slots against simulation time
    plt.figure(figsize=(20, 10))
    plt.plot(free_slots['Time'], free_slots['Free Slots'], color='purple')
    plt.xlabel('Simulation Time in ms')
    plt.ylabel('Free Slots')
    plt.title('Free Slots vs Simulation Time')
    plt.grid(True)
    plt.savefig('../Results/free_slots_vs_simulation_time.png')
    plt.show()

    # Plot rejected sessions against simulation time
    plt.figure(figsize=(20, 10))
    plt.plot(rejected_sessions['Time'], rejected_sessions['Rejected Sessions'], color='black')
    plt.xlabel('Simulation Time in ms')
    plt.ylabel('Rejected Sessions')
    plt.title('Rejected Sessions vs Simulation Time')
    plt.grid(True)
    plt.savefig('../Results/rejected_sessions_vs_simulation_time.png')
    plt.show()

    # Calculate the duration for each interval where the number remains constant
    active_pdus['Duration'] = active_pdus['Time'].diff().shift(-1)
    busy_upfs['Duration'] = busy_upfs['Time'].diff().shift(-1)
    idle_upfs['Duration'] = idle_upfs['Time'].diff().shift(-1)
    free_slots['Duration'] = free_slots['Time'].diff().shift(-1)

    # Drop the last row
    active_pdus = active_pdus.dropna()
    busy_upfs = busy_upfs.dropna()
    idle_upfs = idle_upfs.dropna()
    free_slots = free_slots.dropna()

    # Calculate the weights
    weights_active_pdus = active_pdus['Duration'].values
    weights_busy_upfs = busy_upfs['Duration'].values
    weights_idle_upfs = idle_upfs['Duration'].values
    weights_free_slots = free_slots['Duration'].values

    # Number of bins
    num_bins = 20

    # Calculate the histograms
    pdf_active_pdus, bins_active_pdus = np.histogram(active_pdus['Active PDUs'], bins=num_bins,
                                                     weights=weights_active_pdus, density=True)
    pdf_busy_upfs, bins_busy_upfs = np.histogram(busy_upfs['Busy UPFs'], bins=num_bins, weights=weights_busy_upfs,
                                                 density=True)
    pdf_idle_upfs, bins_idle_upfs = np.histogram(idle_upfs['Idle UPFs'], bins=num_bins, weights=weights_idle_upfs,
                                                 density=True)
    pdf_free_slots, bins_free_slots = np.histogram(free_slots['Free Slots'], bins=num_bins, weights=weights_free_slots,
                                                   density=True)

    # Plot PDF of Active PDUs
    plt.figure(figsize=(20, 10))
    plt.hist(active_pdus['Active PDUs'], bins=bins_active_pdus, weights=weights_active_pdus, density=True, alpha=0.75,
             edgecolor='black')
    plt.title('PDF Weighted by Duration of Active PDUs')
    plt.xlabel('Active PDUs')
    plt.ylabel('Probability Density')
    plt.grid(True)
    plt.savefig('../Results/active_pdus_pdf.png')
    plt.show()

    # Plot PDF of Busy UPFs
    plt.figure(figsize=(20, 10))
    plt.hist(busy_upfs['Busy UPFs'], bins=bins_busy_upfs, weights=weights_busy_upfs, density=True, alpha=0.75,
             edgecolor='black')
    plt.title('PDF Weighted by Duration of Busy UPFs')
    plt.xlabel('Busy UPFs')
    plt.ylabel('Probability Density')
    plt.grid(True)
    plt.savefig('../Results/busy_upfs_pdf.png')
    plt.show()

    # Plot PDF of Idle UPFs
    plt.figure(figsize=(20, 10))
    plt.hist(idle_upfs['Idle UPFs'], bins=bins_idle_upfs, weights=weights_idle_upfs, density=True, alpha=0.75,
             edgecolor='black')
    plt.title('PDF Weighted by Duration of Idle UPFs')
    plt.xlabel('Idle UPFs')
    plt.ylabel('Probability Density')
    plt.grid(True)
    plt.savefig('../Results/idle_upfs_pdf.png')
    plt.show()

    # Plot PDF of Free Slots
    plt.figure(figsize=(20, 10))
    plt.hist(free_slots['Free Slots'], bins=bins_free_slots, weights=weights_free_slots, density=True, alpha=0.75,
             edgecolor='black')
    plt.title('PDF Weighted by Duration of Free Slots')
    plt.xlabel('Free Slots')
    plt.ylabel('Probability Density')
    plt.grid(True)
    plt.savefig('../Results/free_slots_pdf.png')
    plt.show()


if __name__ == "__main__":
    main()
