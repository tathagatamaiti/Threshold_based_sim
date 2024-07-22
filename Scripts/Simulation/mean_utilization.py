import pandas as pd

file_paths = [
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
    '../Data/utilization_12.csv'
]

averages = []

for file_path in file_paths:
    df = pd.read_csv(file_path)
    avg = df.iloc[:, 1].mean()
    averages.append(avg)

averages_df = pd.DataFrame(averages, columns=['Average Utilization'])
averages_df.to_csv('../Data/average_utilization.csv', index=False)
