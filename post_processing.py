import matplotlib.pyplot as plt


def generate_plots(time_points, pdu_counts, upf_counts, active_pdu_counts, active_upf_counts):
    """
    Generate plots for PDU count against simulation time and UPF count against simulation time.

    :param time_points: List of time points
    :param pdu_counts: List of PDUs
    :param upf_counts: List of UPFs
    :param active_pdu_counts: List of active PDUs
    :param active_upf_counts: List of active UPFs
    """
    # Plot PDU against simulation time
    plt.figure(figsize=(10, 6))
    plt.plot(time_points, pdu_counts, label='PDU Count', color='blue')
    plt.xlabel('Simulation Time')
    plt.ylabel('PDU Count')
    plt.title('PDU vs Simulation Time')
    plt.grid(True)
    plt.legend()
    plt.savefig('pdu_vs_simulation_time.png')
    plt.show()

    # Plot UPF against simulation time
    plt.figure(figsize=(10, 6))
    plt.plot(time_points, upf_counts, label='UPF Count', color='green')
    plt.xlabel('Simulation Time')
    plt.ylabel('UPF Count')
    plt.title('UPF vs Simulation Time')
    plt.grid(True)
    plt.legend()
    plt.savefig('upf_vs_simulation_time_case1.png')
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(time_points, active_pdu_counts, label='Active PDUs', color='red')
    plt.xlabel('Simulation Time')
    plt.ylabel('Active PDU Count')
    plt.title('Active PDUs vs Simulation Time')
    plt.grid(True)
    plt.legend()
    plt.savefig('active_pdus_vs_simulation_time_case1.png')
    plt.show()

    # Plot active UPFs against simulation time
    plt.figure(figsize=(10, 6))
    plt.plot(time_points, active_upf_counts, label='Active UPFs', color='orange')
    plt.xlabel('Simulation Time')
    plt.ylabel('Active UPF Count')
    plt.title('Active UPFs vs Simulation Time')
    plt.grid(True)
    plt.legend()
    plt.savefig('active_upfs_vs_simulation_time_case1.png')
    plt.show()
