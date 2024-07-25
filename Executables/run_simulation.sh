#!/bin/bash

# Parameters
DEFAULT_RUN_ID=1
DEFAULT_UPF_CASE=2
DEFAULT_MAX_UPF_INSTANCES=100
DEFAULT_MIN_UPF_INSTANCES=1
DEFAULT_MAX_SESSIONS_PER_UPF=8
SCALE_OUT_THRESHOLD=3
SCALE_IN_THRESHOLD=13
SIMULATION_TIME=3600000
ARRIVAL_RATE_1=0.2
ARRIVAL_RATE_2=4
ARRIVAL_RATE_3=6
ARRIVAL_RATE_4=8
ARRIVAL_RATE_5=10
ARRIVAL_RATE_6=12
ARRIVAL_RATE_7=14
ARRIVAL_RATE_8=16
ARRIVAL_RATE_9=18
ARRIVAL_RATE_10=20
ARRIVAL_RATE_11=22
ARRIVAL_RATE_12=24
ARRIVAL_RATE_13=26
MU=0.02
SCALING_CASE=1
MIGRATION_FREQUENCY=100000
OUTPUT_FILE="simulation"
SEED=42

# Run 1
echo "Running simulation with lambda=${ARRIVAL_RATE_1}"
python3 ../Scripts/Simulation/main_sim.py --run_id ${DEFAULT_RUN_ID} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD} --scale-in-threshold ${SCALE_IN_THRESHOLD} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_1} --mu ${MU} --scaling_case ${SCALING_CASE} --migration_frequency ${MIGRATION_FREQUENCY} --output-file ../Logs/${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_1}.log --seed ${SEED}

# Run 2
NEW_RUN_ID_2=2
echo "Running simulation with lambda=${ARRIVAL_RATE_2}"
python3 ../Scripts/Simulation/main_sim.py --run_id ${NEW_RUN_ID_2} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD} --scale-in-threshold ${SCALE_IN_THRESHOLD} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_2} --mu ${MU} --scaling_case ${SCALING_CASE} --migration_frequency ${MIGRATION_FREQUENCY} --output-file ../Logs/${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_2}.log --seed ${SEED}

# Run 3
NEW_RUN_ID_3=3
echo "Running simulation with lambda=${ARRIVAL_RATE_3}"
python3 ../Scripts/Simulation/main_sim.py --run_id ${NEW_RUN_ID_3} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD} --scale-in-threshold ${SCALE_IN_THRESHOLD} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_3} --mu ${MU} --scaling_case ${SCALING_CASE} --migration_frequency ${MIGRATION_FREQUENCY} --output-file ../Logs/${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_3}.log --seed ${SEED}

# Run 4
NEW_RUN_ID_4=4
echo "Running simulation with lambda=${ARRIVAL_RATE_4}"
python3 ../Scripts/Simulation/main_sim.py --run_id ${NEW_RUN_ID_4} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD} --scale-in-threshold ${SCALE_IN_THRESHOLD} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_4} --mu ${MU} --scaling_case ${SCALING_CASE} --migration_frequency ${MIGRATION_FREQUENCY} --output-file ../Logs/${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_4}.log --seed ${SEED}

# Run 5
NEW_RUN_ID_5=5
echo "Running simulation with lambda=${ARRIVAL_RATE_5}"
python3 ../Scripts/Simulation/main_sim.py --run_id ${NEW_RUN_ID_5} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD} --scale-in-threshold ${SCALE_IN_THRESHOLD} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_5} --mu ${MU} --scaling_case ${SCALING_CASE} --migration_frequency ${MIGRATION_FREQUENCY} --output-file ../Logs/${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_5}.log --seed ${SEED}

# Run 6
NEW_RUN_ID_6=6
echo "Running simulation with lambda=${ARRIVAL_RATE_6}"
python3 ../Scripts/Simulation/main_sim.py --run_id ${NEW_RUN_ID_6} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD} --scale-in-threshold ${SCALE_IN_THRESHOLD} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_6} --mu ${MU} --scaling_case ${SCALING_CASE} --migration_frequency ${MIGRATION_FREQUENCY} --output-file ../Logs/${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_6}.log --seed ${SEED}

# Run 7
NEW_RUN_ID_7=7
echo "Running simulation with lambda=${ARRIVAL_RATE_7}"
python3 ../Scripts/Simulation/main_sim.py --run_id ${NEW_RUN_ID_7} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD} --scale-in-threshold ${SCALE_IN_THRESHOLD} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_7} --mu ${MU} --scaling_case ${SCALING_CASE} --migration_frequency ${MIGRATION_FREQUENCY} --output-file ../Logs/${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_7}.log --seed ${SEED}

# Run 8
NEW_RUN_ID_8=8
echo "Running simulation with lambda=${ARRIVAL_RATE_8}"
python3 ../Scripts/Simulation/main_sim.py --run_id ${NEW_RUN_ID_8} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD} --scale-in-threshold ${SCALE_IN_THRESHOLD} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_8} --mu ${MU} --scaling_case ${SCALING_CASE} --migration_frequency ${MIGRATION_FREQUENCY} --output-file ../Logs/${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_8}.log --seed ${SEED}

# Run 9
NEW_RUN_ID_9=9
echo "Running simulation with lambda=${ARRIVAL_RATE_9}"
python3 ../Scripts/Simulation/main_sim.py --run_id ${NEW_RUN_ID_9} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD} --scale-in-threshold ${SCALE_IN_THRESHOLD} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_9} --mu ${MU} --scaling_case ${SCALING_CASE} --migration_frequency ${MIGRATION_FREQUENCY} --output-file ../Logs/${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_9}.log --seed ${SEED}

# Run 10
NEW_RUN_ID_10=10
echo "Running simulation with lambda=${ARRIVAL_RATE_10}"
python3 ../Scripts/Simulation/main_sim.py --run_id ${NEW_RUN_ID_10} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD} --scale-in-threshold ${SCALE_IN_THRESHOLD} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_10} --mu ${MU} --scaling_case ${SCALING_CASE} --migration_frequency ${MIGRATION_FREQUENCY} --output-file ../Logs/${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_10}.log --seed ${SEED}

# Run 11
NEW_RUN_ID_11=11
echo "Running simulation with lambda=${ARRIVAL_RATE_11}"
python3 ../Scripts/Simulation/main_sim.py --run_id ${NEW_RUN_ID_11} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD} --scale-in-threshold ${SCALE_IN_THRESHOLD} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_11} --mu ${MU} --scaling_case ${SCALING_CASE} --migration_frequency ${MIGRATION_FREQUENCY} --output-file ../Logs/${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_11}.log --seed ${SEED}

# Run 12
NEW_RUN_ID_12=12
echo "Running simulation with lambda=${ARRIVAL_RATE_12}"
python3 ../Scripts/Simulation/main_sim.py --run_id ${NEW_RUN_ID_12} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD} --scale-in-threshold ${SCALE_IN_THRESHOLD} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_12} --mu ${MU} --scaling_case ${SCALING_CASE} --migration_frequency ${MIGRATION_FREQUENCY} --output-file ../Logs/${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_12}.log --seed ${SEED}

# Run 13
NEW_RUN_ID_13=13
echo "Running simulation with lambda=${ARRIVAL_RATE_13}"
python3 ../Scripts/Simulation/main_sim.py --run_id ${NEW_RUN_ID_13} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD} --scale-in-threshold ${SCALE_IN_THRESHOLD} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_13} --mu ${MU} --scaling_case ${SCALING_CASE} --migration_frequency ${MIGRATION_FREQUENCY} --output-file ../Logs/${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_13}.log --seed ${SEED}

# Calculations
python3 ../Scripts/Simulation/calculations.py