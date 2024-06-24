#!/bin/bash

# Parameters
DEFAULT_RUN_ID=1
DEFAULT_UPF_CASE=2
DEFAULT_MAX_UPF_INSTANCES=100
DEFAULT_MIN_UPF_INSTANCES=1
DEFAULT_MAX_SESSIONS_PER_UPF=8
SCALE_OUT_THRESHOLD_1=3
SCALE_IN_THRESHOLD_1=13
SCALE_OUT_THRESHOLD_2=13
SCALE_IN_THRESHOLD_2=23
SIMULATION_TIME=100000
ARRIVAL_RATE_1=50
ARRIVAL_RATE_2=100
ARRIVAL_RATE_3=150
MU=0.0167
MIGRATION_CASE=1
OUTPUT_FILE="simulation"
SEED=42

# Run 1
echo "Running simulation with lambda=${ARRIVAL_RATE_1}, t1=${SCALE_OUT_THRESHOLD_1}, t2=${SCALE_IN_THRESHOLD_1}"
python3 main.py --run_id ${DEFAULT_RUN_ID} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD_1} --scale-in-threshold ${SCALE_IN_THRESHOLD_1} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_1} --mu ${MU} --migration_case ${MIGRATION_CASE} --output-file ${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_1}_T1_${SCALE_OUT_THRESHOLD_1}_T2_${SCALE_IN_THRESHOLD_1}.log --seed ${SEED}

# Run 2
NEW_RUN_ID_2=2
echo "Running simulation with lambda=${ARRIVAL_RATE_1}, t1=${SCALE_OUT_THRESHOLD_2}, t2=${SCALE_IN_THRESHOLD_2}"
python3 main.py --run_id ${NEW_RUN_ID_2} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD_2} --scale-in-threshold ${SCALE_IN_THRESHOLD_2} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_1} --mu ${MU} --migration_case ${MIGRATION_CASE} --output-file ${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_1}_T1_${SCALE_OUT_THRESHOLD_2}_T2_${SCALE_IN_THRESHOLD_2}.log --seed ${SEED}

# Run 3
NEW_RUN_ID_3=3
echo  "Running simulation with lambda=${ARRIVAL_RATE_2}, t1=${SCALE_OUT_THRESHOLD_1}, t2=${SCALE_IN_THRESHOLD_1}"
python3 main.py --run_id ${NEW_RUN_ID_3} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD_1} --scale-in-threshold ${SCALE_IN_THRESHOLD_1} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_2} --mu ${MU} --migration_case ${MIGRATION_CASE} --output-file ${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_2}_T1_${SCALE_OUT_THRESHOLD_1}_T2_${SCALE_IN_THRESHOLD_1}.log --seed ${SEED}

# Run 4
NEW_RUN_ID_4=4
echo  "Running simulation with lambda=${ARRIVAL_RATE_2}, t1=${SCALE_OUT_THRESHOLD_2}, t2=${SCALE_IN_THRESHOLD_2}"
python3 main.py --run_id ${NEW_RUN_ID_4} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD_2} --scale-in-threshold ${SCALE_IN_THRESHOLD_2} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_2} --mu ${MU} --migration_case ${MIGRATION_CASE} --output-file ${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_2}_T1_${SCALE_OUT_THRESHOLD_2}_T2_${SCALE_IN_THRESHOLD_2}.log --seed ${SEED}

# Run 5
NEW_RUN_ID_4=5
echo  "Running simulation with lambda=${ARRIVAL_RATE_3}, t1=${SCALE_OUT_THRESHOLD_1}, t2=${SCALE_IN_THRESHOLD_1}"
python3 main.py --run_id ${NEW_RUN_ID_4} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD_1} --scale-in-threshold ${SCALE_IN_THRESHOLD_1} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_3} --mu ${MU} --migration_case ${MIGRATION_CASE} --output-file ${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_3}_T1_${SCALE_OUT_THRESHOLD_1}_T2_${SCALE_IN_THRESHOLD_1}.log --seed ${SEED}

# Run 6
NEW_RUN_ID_4=6
echo  "Running simulation with lambda=${ARRIVAL_RATE_3}, t1=${SCALE_OUT_THRESHOLD_2}, t2=${SCALE_IN_THRESHOLD_2}"
python3 main.py --run_id ${NEW_RUN_ID_4} --upf_case ${DEFAULT_UPF_CASE} --max-upf-instances ${DEFAULT_MAX_UPF_INSTANCES} --min-upf-instances ${DEFAULT_MIN_UPF_INSTANCES} --max-sessions-per-upf ${DEFAULT_MAX_SESSIONS_PER_UPF} --scale-out-threshold ${SCALE_OUT_THRESHOLD_2} --scale-in-threshold ${SCALE_IN_THRESHOLD_2} --simulation-time ${SIMULATION_TIME} --arrival_rate ${ARRIVAL_RATE_3} --mu ${MU} --migration_case ${MIGRATION_CASE} --output-file ${OUTPUT_FILE}_lambda_${ARRIVAL_RATE_3}_T1_${SCALE_OUT_THRESHOLD_2}_T2_${SCALE_IN_THRESHOLD_2}.log --seed ${SEED}

echo "All simulations completed."
