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
ARRIVAL_RATE_1=4
ARRIVAL_RATE_2=6
ARRIVAL_RATE_3=8
ARRIVAL_RATE_4=10
ARRIVAL_RATE_5=12
ARRIVAL_RATE_6=14
ARRIVAL_RATE_7=15
MU=0.02
MIGRATION_CASE=1
OUTPUT_FILE="simulation"
SEED=42

# Run 1
echo "Running simulation with lambda=${ARRIVAL_RATE_1}"
python3 main.py --run_id ${DEFAULT_RUN_ID} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD} --scale-in-threshold ${SCALE_IN_THRESHOLD} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_1} --mu ${MU} --migration_case ${MIGRATION_CASE} --output-file ${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_1}.log --seed ${SEED}

# Run 2
NEW_RUN_ID_2=2
echo "Running simulation with lambda=${ARRIVAL_RATE_2}"
python3 main.py --run_id ${NEW_RUN_ID_2} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD} --scale-in-threshold ${SCALE_IN_THRESHOLD} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_2} --mu ${MU} --migration_case ${MIGRATION_CASE} --output-file ${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_2}.log --seed ${SEED}

# Run 3
NEW_RUN_ID_3=3
echo  "Running simulation with lambda=${ARRIVAL_RATE_3}"
python3 main.py --run_id ${NEW_RUN_ID_3} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD} --scale-in-threshold ${SCALE_IN_THRESHOLD} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_3} --mu ${MU} --migration_case ${MIGRATION_CASE} --output-file ${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_3}.log --seed ${SEED}

# Run 4
NEW_RUN_ID_4=4
echo  "Running simulation with lambda=${ARRIVAL_RATE_4}"
python3 main.py --run_id ${NEW_RUN_ID_4} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD} --scale-in-threshold ${SCALE_IN_THRESHOLD} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_4} --mu ${MU} --migration_case ${MIGRATION_CASE} --output-file ${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_4}.log --seed ${SEED}

# Run 5
NEW_RUN_ID_5=5
echo  "Running simulation with lambda=${ARRIVAL_RATE_5}"
python3 main.py --run_id ${NEW_RUN_ID_5} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD} --scale-in-threshold ${SCALE_IN_THRESHOLD} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_5} --mu ${MU} --migration_case ${MIGRATION_CASE} --output-file ${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_5}.log --seed ${SEED}

# Run 6
NEW_RUN_ID_6=6
echo  "Running simulation with lambda=${ARRIVAL_RATE_6}"
python3 main.py --run_id ${NEW_RUN_ID_6} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD} --scale-in-threshold ${SCALE_IN_THRESHOLD} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_6} --mu ${MU} --migration_case ${MIGRATION_CASE} --output-file ${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_6}.log --seed ${SEED}

NEW_RUN_ID_7=7
echo  "Running simulation with lambda=${ARRIVAL_RATE_7}"
python3 main.py --run_id ${NEW_RUN_ID_7} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD} --scale-in-threshold ${SCALE_IN_THRESHOLD} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_7} --mu ${MU} --migration_case ${MIGRATION_CASE} --output-file ${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_7}.log --seed ${SEED}
echo "All simulations completed."
