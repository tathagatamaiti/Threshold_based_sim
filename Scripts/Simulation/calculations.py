import pandas as pd

file_paths_utilization = [
    '../Data/utilization_1.csv',
    '../Data/utilization_2.csv',
    '../Data/utilization_3.csv',
    '../Data/utilization_4.csv',
    '../Data/utilization_5.csv',
    '../Data/utilization_6.csv',
    '../Data/utilization_7.csv',
    '../Data/utilization_8.csv',
    '../Data/utilization_9.csv',
    '../Data/utilization_10.csv',
    '../Data/utilization_11.csv',
    '../Data/utilization_12.csv',
    '../Data/utilization_13.csv'
]
averages = []
for file_path_utilization in file_paths_utilization:
    df_utilization = pd.read_csv(file_path_utilization)
    avg = df_utilization.iloc[:, 1].mean()
    averages.append(avg)
averages_df = pd.DataFrame(averages, columns=['Average Utilization'])
averages_df.to_csv('../Data/average_utilization.csv', index=False)

file_paths_sim_data = [
    '../Data/sim_data_1.csv',
    '../Data/sim_data_2.csv',
    '../Data/sim_data_3.csv',
    '../Data/sim_data_4.csv',
    '../Data/sim_data_5.csv',
    '../Data/sim_data_6.csv',
    '../Data/sim_data_7.csv',
    '../Data/sim_data_8.csv',
    '../Data/sim_data_9.csv',
    '../Data/sim_data_10.csv',
    '../Data/sim_data_11.csv',
    '../Data/sim_data_12.csv',
    '../Data/sim_data_13.csv'
]
accepted_percentages = []
rejected_percentages = []
for file_path_sim_data in file_paths_sim_data:
    df_sim_data = pd.read_csv(file_path_sim_data)
    accepted_percentage = (df_sim_data.iloc[:, 2] / df_sim_data.iloc[:, 0]) * 100
    accepted_percentages.append(accepted_percentage.mean())
    rejected_percentage = (df_sim_data.iloc[:, 1] / df_sim_data.iloc[:, 0]) * 100
    rejected_percentages.append(rejected_percentage.mean())
accepted_df = pd.DataFrame({'Percentage of PDU Acceptance': accepted_percentages})
rejected_df = pd.DataFrame({'Percentage of PDU Rejection': rejected_percentages})
accepted_df.to_csv('../Data/accepted_percentages.csv', index=False)
rejected_df.to_csv('../Data/rejected_percentages.csv', index=False)

