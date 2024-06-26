import matplotlib.pyplot as plt
import argparse
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

    # Group and sum the durations
    duration_by_pdu = active_pdus.groupby('Active PDUs')['Duration'].sum()
    duration_by_busy_upf = busy_upfs.groupby('Busy UPFs')['Duration'].sum()
    duration_by_idle_upf = idle_upfs.groupby('Idle UPFs')['Duration'].sum()
    duration_by_free_slots = free_slots.groupby('Free Slots')['Duration'].sum()

    # Normalize by the total time to get the PDF
    total_time = duration_by_pdu.sum()
    pdf_by_pdu = duration_by_pdu / total_time

    total_time = duration_by_busy_upf.sum()
    pdf_by_busy_upf = duration_by_busy_upf / total_time

    total_time = duration_by_idle_upf.sum()
    pdf_by_idle_upf = duration_by_idle_upf / total_time

    total_time = duration_by_free_slots.sum()
    pdf_by_free_slots = duration_by_free_slots / total_time

    # Convert to a DataFrame for better readability
    pdf_pdu = pdf_by_pdu.reset_index().rename(columns={'Duration': 'PDF'})
    pdf_busy_upf = pdf_by_busy_upf.reset_index().rename(columns={'Duration': 'PDF'})
    pdf_idle_upf = pdf_by_idle_upf.reset_index().rename(columns={'Duration': 'PDF'})
    pdf_free_slots = pdf_by_free_slots.reset_index().rename(columns={'Duration': 'PDF'})

    # Plot the PDF of active PDUs
    plt.figure(figsize=(20, 10))
    plt.bar(pdf_pdu['Active PDUs'], pdf_pdu['PDF'], edgecolor='k', alpha=0.7)
    plt.xlabel('Active PDUs')
    plt.ylabel('PDF')
    plt.title('Probability Density Function of Active PDUs')
    plt.xticks(pdf_pdu['Active PDUs'])
    plt.savefig('../Results/active_pdus_pdf.png')
    plt.show()

    # Plot the PDF of busy UPFs
    plt.figure(figsize=(20, 10))
    plt.bar(pdf_busy_upf['Busy UPFs'], pdf_busy_upf['PDF'], edgecolor='k', alpha=0.7)
    plt.xlabel('Busy UPFs')
    plt.ylabel('PDF')
    plt.title('Probability Density Function of Busy UPFs')
    plt.xticks(pdf_busy_upf['Busy UPFs'])
    plt.savefig('../Results/busy_upfs_pdf.png')
    plt.show()

    # Plot the PDF of idle UPFs
    plt.figure(figsize=(20, 10))
    plt.bar(pdf_idle_upf['Idle UPFs'], pdf_idle_upf['PDF'], edgecolor='k', alpha=0.7)
    plt.xlabel('Idle UPFs')
    plt.ylabel('PDF')
    plt.title('Probability Density Function of Busy UPFs')
    plt.xticks(pdf_idle_upf['Idle UPFs'])
    plt.savefig('../Results/idle_upfs_pdf.png')
    plt.show()

    # Plot the PDF of Free Slots
    plt.figure(figsize=(20, 10))
    plt.bar(pdf_free_slots['Free Slots'], pdf_free_slots['PDF'], edgecolor='k', alpha=0.7)
    plt.xlabel('Free Slots')
    plt.ylabel('PDF')
    plt.title('Probability Density Function of Free Slots')
    plt.xticks(pdf_free_slots['Free Slots'])
    plt.savefig('../Results/free_slots_pdf.png')
    plt.show()


if __name__ == "__main__":
    main()
