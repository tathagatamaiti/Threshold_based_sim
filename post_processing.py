import matplotlib.pyplot as plt
import argparse
import numpy as np
import pandas as pd
import scipy.stats as stats


def main():
    parser = argparse.ArgumentParser(description='Post-process simulation results')
    parser.add_argument('--input-files', type=str, nargs=8, required=True, help='Input CSV files to process')
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
    session_durations = pd.read_csv(input_files[7])

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

    # Plot PDF of Active PDUs
    active_pdus['Duration'] = active_pdus['Time'].diff().fillna(0)
    weighted_active_pdus, bins_active_pdus = np.histogram(active_pdus['Active PDUs'],
                                                          bins=range(int(active_pdus['Active PDUs'].max()) + 2),
                                                          weights=active_pdus['Duration'], density=True)
    total_weight_active_pdus = sum(weighted_active_pdus)
    pdf_active_pdus = weighted_active_pdus / total_weight_active_pdus
    plt.figure(figsize=(20, 10))
    plt.bar(bins_active_pdus[:-1], pdf_active_pdus, width=1, edgecolor='black', alpha=0.7, align='edge')
    plt.xlabel('Active PDUs')
    plt.ylabel('Probability')
    plt.title('PDF Weighted by Duration of Active PDUs')
    plt.grid(True)
    plt.savefig('../Results/active_pdus_pdf.png')
    plt.show()

    # Plot PDF of Busy UPFs
    busy_upfs['Duration'] = busy_upfs['Time'].diff().fillna(0)
    weighted_busy_upfs, bins_busy_upfs = np.histogram(busy_upfs['Busy UPFs'], weights=busy_upfs['Duration'],
                                                      bins=range(int(busy_upfs['Busy UPFs'].max()) + 2))
    total_weight_busy_upfs = sum(weighted_busy_upfs)
    pdf_busy_upfs = weighted_busy_upfs / total_weight_busy_upfs
    plt.figure(figsize=(20, 10))
    plt.bar(bins_busy_upfs[:-1], pdf_busy_upfs, width=1, edgecolor='black', alpha=0.7, align='edge')
    plt.xlabel('Busy UPFs')
    plt.ylabel('Probability')
    plt.title('Probability Distribution Function of Busy UPFs')
    plt.grid(True)
    plt.savefig('../Results/busy_upfs_pdf.png')
    plt.show()

    # Plot PDF of Idle UPFs
    idle_upfs['Duration'] = idle_upfs['Time'].diff().fillna(0)
    weighted_idle_upfs, bins_idle_upfs = np.histogram(idle_upfs['Idle UPFs'], weights=idle_upfs['Duration'],
                                                      bins=range(int(idle_upfs['Idle UPFs'].max()) + 2))
    total_weight_idle_upfs = sum(weighted_idle_upfs)
    pdf_idle_upfs = weighted_idle_upfs / total_weight_idle_upfs
    plt.figure(figsize=(20, 10))
    plt.bar(bins_idle_upfs[:-1], pdf_idle_upfs, width=1, edgecolor='black', alpha=0.7, align='edge')
    plt.xlabel('Idle UPFs')
    plt.ylabel('Probability')
    plt.title('Probability Distribution Function of Idle UPFs')
    plt.grid(True)
    plt.savefig('../Results/idle_upfs_pdf.png')
    plt.show()

    # Plot PDF of Free Slots
    free_slots['Duration'] = free_slots['Time'].diff().fillna(0)
    weighted_free_slots, bins_free_slots = np.histogram(free_slots['Free Slots'], weights=free_slots['Duration'],
                                                        bins=range(int(free_slots['Free Slots'].max()) + 2))
    total_weight_free_slots = sum(weighted_free_slots)
    pdf_free_slots = weighted_free_slots / total_weight_free_slots
    plt.figure(figsize=(20, 10))
    plt.bar(bins_free_slots[:-1], pdf_free_slots, width=1, edgecolor='black', alpha=0.7, align='edge')
    plt.xlabel('Free Slots')
    plt.ylabel('Probability')
    plt.title('Probability Distribution Function of Free Slots')
    plt.grid(True)
    plt.savefig('../Results/free_slots_pdf.png')
    plt.show()

    # Plot Poisson distributions
    durations_empirical = session_durations['Duration (seconds)']
    mean_empirical = durations_empirical.mean()
    poisson_empirical = stats.poisson(mu=mean_empirical)
    x_values = np.arange(0, durations_empirical.max() + 1)
    pmf_empirical_values = poisson_empirical.pmf(x_values)

    mu_exponential = 0.02
    mean_theoretical = 1 / mu_exponential
    poisson_theoretical = stats.poisson(mu=mean_theoretical)
    pmf_theoretical_values = poisson_theoretical.pmf(x_values)

    plt.figure(figsize=(20, 10))
    plt.plot(x_values, pmf_empirical_values, 'bo', ms=8, label='Empirical Poisson PMF')
    plt.vlines(x_values, 0, pmf_empirical_values, colors='b', lw=2)

    plt.plot(x_values, pmf_theoretical_values, 'ro', ms=8, label='Theoretical Poisson PMF')
    plt.vlines(x_values, 0, pmf_theoretical_values, colors='r', lw=2)

    plt.title('Empirical vs Theoretical Poisson Distribution of Session Durations')
    plt.xlabel('Duration (seconds)')
    plt.ylabel('Probability')
    plt.legend()
    plt.grid(True)
    plt.savefig('../Results/poisson_duration.png')
    plt.show()

    inter_arrival_times_empirical = pdus['Time'].diff().dropna()
    mean_empirical_inter_arrival = inter_arrival_times_empirical.mean()
    poisson_empirical_inter_arrival = stats.poisson(mu=mean_empirical_inter_arrival)
    x_values_inter_arrival = np.arange(0, inter_arrival_times_empirical.max() + 1)
    pmf_empirical_values_inter_arrival = poisson_empirical_inter_arrival.pmf(x_values_inter_arrival)

    lambda_exponential_inter_arrival = 1/26
    mean_theoretical_inter_arrival = 1 / lambda_exponential_inter_arrival
    poisson_theoretical_inter_arrival = stats.poisson(mu=mean_theoretical_inter_arrival)
    pmf_theoretical_values_inter_arrival = poisson_theoretical_inter_arrival.pmf(x_values_inter_arrival)

    plt.figure(figsize=(20, 10))
    plt.plot(x_values_inter_arrival, pmf_empirical_values_inter_arrival, 'bo', ms=8, label='Empirical Poisson PMF')
    plt.vlines(x_values_inter_arrival, 0, pmf_empirical_values_inter_arrival, colors='b', lw=2)

    plt.plot(x_values_inter_arrival, pmf_theoretical_values_inter_arrival, 'ro', ms=8, label='Theoretical Poisson PMF')
    plt.vlines(x_values_inter_arrival, 0, pmf_theoretical_values_inter_arrival, colors='r', lw=2)

    plt.title('Empirical vs Theoretical Poisson Distribution of Inter-Arrival Times')
    plt.xlabel('Inter-Arrival Time (seconds)')
    plt.ylabel('Probability')
    plt.legend()
    plt.grid(True)
    plt.savefig('../Results/poisson_inter_arrival.png')
    plt.show()


if __name__ == "__main__":
    main()
