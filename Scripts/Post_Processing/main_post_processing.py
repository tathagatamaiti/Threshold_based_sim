import matplotlib.pyplot as plt
import argparse
import numpy as np
import pandas as pd
import scipy.stats as stats


def main():
    parser = argparse.ArgumentParser(description='Post-process simulation results')
    parser.add_argument('--input-files', type=str, nargs=11, required=True, help='Input CSV files to process')
    args = parser.parse_args()

    process_results(args.input_files)


def process_results(input_files):
    # Read data from CSV files
    pdus = pd.read_csv(input_files[0])
    upfs = pd.read_csv(input_files[1])
    active_pdus = pd.read_csv(input_files[2])
    deployed_upfs = pd.read_csv(input_files[3])
    busy_upfs = pd.read_csv(input_files[4])
    idle_upfs = pd.read_csv(input_files[5])
    free_slots = pd.read_csv(input_files[6])
    session_durations = pd.read_csv(input_files[7])
    inter_arrival_times = pd.read_csv(input_files[8])
    average_utilization = pd.read_csv(input_files[9])
    session_throughput = pd.read_csv(input_files[10])

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

    # Plot PDF of Active PDUs
    active_pdus['Duration'] = active_pdus['Time'].diff().fillna(0)
    weighted_active_pdus, bins_active_pdus = np.histogram(active_pdus['Active PDUs'],
                                                          bins=range(int(active_pdus['Active PDUs'].max()) + 2),
                                                          weights=active_pdus['Duration'], density=True)
    total_weight_active_pdus = sum(weighted_active_pdus)
    pdf_active_pdus = weighted_active_pdus / total_weight_active_pdus
    plt.figure(figsize=(20, 10))
    plt.bar(bins_active_pdus[:-1], pdf_active_pdus, width=0.8, edgecolor='black', alpha=0.7, align='edge')
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
    plt.bar(bins_busy_upfs[:-1], pdf_busy_upfs, width=0.8, edgecolor='black', alpha=0.7, align='edge')
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
    plt.bar(bins_idle_upfs[:-1], pdf_idle_upfs, width=0.8, edgecolor='black', alpha=0.7, align='edge')
    plt.xlabel('Idle UPFs')
    plt.ylabel('Probability')
    plt.title('Probability Distribution Function of Idle UPFs')
    plt.grid(True)
    plt.savefig('../Results/idle_upfs_pdf.png')
    plt.show()

    # Plot PDF of Deployed UPFs
    deployed_upfs['Duration'] = deployed_upfs['Time'].diff().fillna(0)
    weighted_deployed_upfs, bins_deployed_upfs = np.histogram(deployed_upfs['Deployed UPFs'],
                                                              weights=deployed_upfs['Duration'],
                                                              bins=range(int(deployed_upfs['Deployed UPFs'].max()) + 2))
    total_weight_deployed_upfs = sum(weighted_deployed_upfs)
    pdf_deployed_upfs = weighted_deployed_upfs / total_weight_deployed_upfs
    plt.figure(figsize=(20, 10))
    plt.bar(bins_deployed_upfs[:-1], pdf_deployed_upfs, width=0.8, edgecolor='black', alpha=0.7, align='edge')
    plt.xlabel('Deployed UPFs')
    plt.ylabel('Probability')
    plt.title('Probability Distribution Function of Deployed UPFs')
    plt.grid(True)
    plt.savefig('../Results/deployed_upfs_pdf.png')
    plt.show()

    # Plot PDF of Busy and Deployed UPFs
    plt.figure(figsize=(20, 10))
    plt.bar(bins_busy_upfs[:-1], pdf_busy_upfs, width=0.8, edgecolor='black', alpha=0.7, align='edge',
            label='Busy UPFs', color='blue')
    plt.bar(bins_deployed_upfs[:-1] + 0.4, pdf_deployed_upfs, width=0.8, edgecolor='black', alpha=0.7, align='edge',
            label='Deployed UPFs', color='green')
    plt.xlabel('UPFs')
    plt.ylabel('Probability')
    plt.title('Probability Distribution Function of Busy and Deployed UPFs')
    plt.grid(True)
    plt.legend()
    plt.savefig('../Results/busy_and_deployed_upfs_pdf.png')
    plt.show()

    # Plot PDF of Free Slots
    free_slots['Duration'] = free_slots['Time'].diff().fillna(0)
    weighted_free_slots, bins_free_slots = np.histogram(free_slots['Free Slots'], weights=free_slots['Duration'],
                                                        bins=range(int(free_slots['Free Slots'].max()) + 2))
    total_weight_free_slots = sum(weighted_free_slots)
    pdf_free_slots = weighted_free_slots / total_weight_free_slots
    plt.figure(figsize=(20, 10))
    plt.bar(bins_free_slots[:-1], pdf_free_slots, width=0.8, edgecolor='black', alpha=0.7, align='edge')
    plt.xlabel('Free Slots')
    plt.ylabel('Probability')
    plt.title('Probability Distribution Function of Free Slots')
    plt.grid(True)
    plt.savefig('../Results/free_slots_pdf.png')
    plt.show()

    # Plot distributions

    inter_arrival_times = inter_arrival_times['Inter-arrival Time'].dropna()

    plt.figure(figsize=(20, 10))
    plt.hist(inter_arrival_times, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
    plt.title('Frequency Distribution of Inter-arrival Times')
    plt.xlabel('Inter-arrival Time')
    plt.ylabel('Density')
    plt.grid(True)
    plt.savefig('../Results/inter_arrival_times_distribution.png')
    plt.show()

    loc, scale = stats.expon.fit(inter_arrival_times)
    pdf_expon = stats.expon.pdf(np.sort(inter_arrival_times), loc, scale)

    plt.figure(figsize=(20, 10))
    plt.hist(inter_arrival_times, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
    plt.plot(np.sort(inter_arrival_times), pdf_expon, 'r-', lw=2)
    plt.title('Frequency Distribution of Inter-arrival Times with Fitted Exponential Distribution')
    plt.xlabel('Inter-arrival Time')
    plt.ylabel('Density')
    plt.grid(True)
    plt.savefig('../Results/inter_arrival_times_distribution_fitted.png')
    plt.show()

    session_durations = session_durations['Duration (seconds)'].dropna()

    plt.figure(figsize=(20, 10))
    plt.hist(session_durations, bins=30, density=True, alpha=0.6, color='b', edgecolor='black')
    plt.title('Frequency Distribution of Session Durations')
    plt.xlabel('Duration (seconds)')
    plt.ylabel('Density')
    plt.grid(True)
    plt.savefig('../Results/session_durations_distribution.png')
    plt.show()

    loc_sess, scale_sess = stats.expon.fit(session_durations)
    pdf_expon_sess = stats.expon.pdf(np.sort(session_durations), loc_sess, scale_sess)

    plt.figure(figsize=(20, 10))
    plt.hist(session_durations, bins=30, density=True, alpha=0.6, color='b', edgecolor='black')
    plt.plot(np.sort(session_durations), pdf_expon_sess, 'r-', lw=2)
    plt.title('Frequency Distribution of Session Durations with Fitted Exponential Distribution')
    plt.xlabel('Duration (seconds)')
    plt.ylabel('Density')
    plt.grid(True)
    plt.savefig('../Results/session_durations_distribution_fitted.png')
    plt.show()

    session_throughput = session_throughput['Throughput'].dropna()

    plt.figure(figsize=(20, 10))
    plt.hist(session_throughput, bins=30, density=True, alpha=0.6, color='b', edgecolor='black')
    plt.title('Frequency Distribution of Session Throughput')
    plt.xlabel('Throughput')
    plt.ylabel('Density')
    plt.grid(True)
    plt.savefig('../Results/session_throughput_distribution.png')
    plt.show()

    loc_sess, scale_sess = stats.expon.fit(session_throughput)
    pdf_expon_sess = stats.expon.pdf(np.sort(session_throughput), loc_sess, scale_sess)

    plt.figure(figsize=(20, 10))
    plt.hist(session_throughput, bins=30, density=True, alpha=0.6, color='b', edgecolor='black')
    plt.plot(np.sort(session_throughput), pdf_expon_sess, 'r-', lw=2)
    plt.title('Frequency Distribution of Session Throughput with Fitted Exponential Distribution')
    plt.xlabel('Throughput')
    plt.ylabel('Density')
    plt.grid(True)
    plt.savefig('../Results/session_throughput_distribution_fitted.png')
    plt.show()

    traffic_intensity = [200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300]
    plt.figure(figsize=(20, 10))
    plt.plot(average_utilization['Average Utilization'], marker='o', linestyle='-')
    plt.title('Average Utilization for Each Traffic Intensity')
    plt.xlabel('Traffic Intensity (λ/µ)')
    plt.ylabel('Average Utilization')
    plt.grid(True)
    plt.xticks(range(len(average_utilization)), traffic_intensity[:len(average_utilization)])
    plt.tight_layout()
    plt.savefig('../Results/average_utilization_traffic_intensity_throughput.png')
    plt.show()


if __name__ == "__main__":
    main()
