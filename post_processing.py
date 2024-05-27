import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde


def generate_plots_case0(time_points, pdu_counts, upf_counts, active_pdu_counts, active_upf_counts):
    """
    Generate plots for PDU count against simulation time and UPF count against simulation time.

    :param time_points: List of time points
    :param pdu_counts: List of PDUs
    :param upf_counts: List of UPFs
    :param active_pdu_counts: List of active PDUs
    :param active_upf_counts: List of active UPFs
    """

    kde_pdu = gaussian_kde(active_pdu_counts)
    pdu_values = np.linspace(min(active_pdu_counts), max(active_pdu_counts), 1000)
    pdu_pdf = kde_pdu(pdu_values)

    kde_upf = gaussian_kde(active_upf_counts)
    upf_values = np.linspace(min(active_upf_counts), max(active_upf_counts), 1000)
    upf_pdf = kde_upf(upf_values)

    # Plot PDU against simulation time
    plt.figure(figsize=(10, 6))
    plt.plot(time_points, pdu_counts, label='PDU Count', color='blue')
    plt.xlabel('Simulation Time')
    plt.ylabel('PDUs')
    plt.title('PDU for case 0 vs Simulation Time')
    plt.grid(True)
    plt.legend()
    plt.savefig('pdu_vs_simulation_time_case0.png')
    plt.show()

    # Plot UPF against simulation time
    plt.figure(figsize=(10, 6))
    plt.plot(time_points, upf_counts, label='UPF Count', color='green')
    plt.xlabel('Simulation Time')
    plt.ylabel('UPFs')
    plt.title('UPF for case 0 vs Simulation Time')
    plt.grid(True)
    plt.legend()
    plt.savefig('upf_vs_simulation_time_case0.png')
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(time_points, active_pdu_counts, label='Active PDUs', color='red')
    plt.xlabel('Simulation Time')
    plt.ylabel('Active PDUs')
    plt.title('Active PDUs for case 0 vs Simulation Time')
    plt.grid(True)
    plt.legend()
    plt.savefig('active_pdus_vs_simulation_time_case0.png')
    plt.show()

    # Plot active UPFs against simulation time
    plt.figure(figsize=(10, 6))
    plt.plot(time_points, active_upf_counts, label='Active UPFs', color='orange')
    plt.xlabel('Simulation Time')
    plt.ylabel('Active UPFs')
    plt.title('Active UPFs for case 0 vs Simulation Time')
    plt.grid(True)
    plt.legend()
    plt.savefig('active_upfs_vs_simulation_time_case0.png')
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(pdu_values, pdu_pdf, label='PDU PDF', color='blue')
    plt.xlabel('PDUs')
    plt.ylabel('Probability Density')
    plt.title('PDF for case 0 for PDUs')
    plt.grid(True)
    plt.legend()
    plt.savefig('pdu_pdf_case0.png')
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(upf_values, upf_pdf, label='UPF PDF', color='green')
    plt.xlabel('UPFs')
    plt.ylabel('Probability Density')
    plt.title('PDF for case 0 for UPFs')
    plt.grid(True)
    plt.legend()
    plt.savefig('upf_pdf_case0.png')
    plt.show()


def generate_plots_case1(time_points, pdu_counts, upf_counts, active_pdu_counts, active_upf_counts):
    """
    Generate plots for PDU count against simulation time and UPF count against simulation time.

    :param time_points: List of time points
    :param pdu_counts: List of PDUs
    :param upf_counts: List of UPFs
    :param active_pdu_counts: List of active PDUs
    :param active_upf_counts: List of active UPFs
    """

    kde_pdu = gaussian_kde(active_pdu_counts)
    pdu_values = np.linspace(min(active_pdu_counts), max(active_pdu_counts), 1000)
    pdu_pdf = kde_pdu(pdu_values)

    kde_upf = gaussian_kde(active_upf_counts)
    upf_values = np.linspace(min(active_upf_counts), max(active_upf_counts), 1000)
    upf_pdf = kde_upf(upf_values)

    # Plot PDU against simulation time
    plt.figure(figsize=(10, 6))
    plt.plot(time_points, pdu_counts, label='PDU Count', color='blue')
    plt.xlabel('Simulation Time')
    plt.ylabel('PDUs')
    plt.title('PDU for case 1 vs Simulation Time')
    plt.grid(True)
    plt.legend()
    plt.savefig('pdu_vs_simulation_time_case1.png')
    plt.show()

    # Plot UPF against simulation time
    plt.figure(figsize=(10, 6))
    plt.plot(time_points, upf_counts, label='UPF Count', color='green')
    plt.xlabel('Simulation Time')
    plt.ylabel('UPFs')
    plt.title('UPF for case 1 vs Simulation Time')
    plt.grid(True)
    plt.legend()
    plt.savefig('upf_vs_simulation_time_case1.png')
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(time_points, active_pdu_counts, label='Active PDUs', color='red')
    plt.xlabel('Simulation Time')
    plt.ylabel('Active PDUs')
    plt.title('Active PDUs for case 1 vs Simulation Time')
    plt.grid(True)
    plt.legend()
    plt.savefig('active_pdus_vs_simulation_time_case1.png')
    plt.show()

    # Plot active UPFs against simulation time
    plt.figure(figsize=(10, 6))
    plt.plot(time_points, active_upf_counts, label='Active UPFs', color='orange')
    plt.xlabel('Simulation Time')
    plt.ylabel('Active UPFs')
    plt.title('Active UPFs for case 1 vs Simulation Time')
    plt.grid(True)
    plt.legend()
    plt.savefig('active_upfs_vs_simulation_time_case1.png')
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(pdu_values, pdu_pdf, label='PDU PDF', color='blue')
    plt.xlabel('PDUs')
    plt.ylabel('Probability Density')
    plt.title('PDF for case 1 for PDUs')
    plt.grid(True)
    plt.legend()
    plt.savefig('pdu_pdf_case1.png')
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(upf_values, upf_pdf, label='UPF PDF', color='green')
    plt.xlabel('UPFs')
    plt.ylabel('Probability Density')
    plt.title('PDF for case 1 for UPFs')
    plt.grid(True)
    plt.legend()
    plt.savefig('upf_pdf_case1.png')
    plt.show()
