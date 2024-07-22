import argparse
from scheduler import Scheduler

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Event-based scheduler simulation")
    parser.add_argument("--run_id", type=int, help="ID of simulation run")
    parser.add_argument("--upf_case", type=int, help="Case for UPF sorting")
    parser.add_argument("--max-upf-instances", type=int, help="Maximum number of UPF instances (L)")
    parser.add_argument("--min-upf-instances", type=int, help="Minimum number of UPF instances (M)")
    parser.add_argument("--max-sessions-per-upf", type=int, help="Maximum number of sessions per UPF (C)")
    parser.add_argument("--scale-out-threshold", type=int, help="Scale-out threshold (T1)")
    parser.add_argument("--scale-in-threshold", type=int, help="Scale-in threshold (T2)")
    parser.add_argument("--simulation-time", type=int, help="Simulation time in milliseconds")
    parser.add_argument("--arrival_rate", type=float, help="Inter-arrival rate in seconds (λ)")
    parser.add_argument("--mu", type=float, help="parameter for session duration in seconds (µ)")
    parser.add_argument("--migration_case", type=int, help="Case for session migration")
    parser.add_argument("--throughput_rate", type=float, help="Rate for PDU session throughput (β)")
    parser.add_argument("--upf_throughput_capacity", type=float, help="Throughput capacity of each UPF instance")
    parser.add_argument("--output-file", type=str, help="File to write simulation outputs")
    parser.add_argument("--seed", type=int, help="Seed for random number generation")

    args = parser.parse_args()

    scheduler = Scheduler(args.run_id, args.upf_case, args.max_upf_instances, args.min_upf_instances,
                          args.max_sessions_per_upf, args.scale_out_threshold, args.scale_in_threshold,
                          args.simulation_time, args.arrival_rate, args.mu, args.migration_case, args.throughput_rate,
                          args.upf_throughput_capacity, args.output_file,
                          args.seed)
    scheduler.run()
