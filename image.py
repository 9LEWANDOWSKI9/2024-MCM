import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

file_path = 'match_2023-wimbledon-1701.csv'
df = pd.read_csv(file_path)

time_column = df.iloc[:, 3]

def time_to_seconds(time_str):
    time_components = [int(x) for x in time_str.split(':')]
    return time_components[0] * 3600 + time_components[1] * 60 + time_components[2]
df['elapsed_time'] = time_column.apply(time_to_seconds)


column_before_last = df.iloc[:, -2]
last_column = df.iloc[:, 3]

plt.plot(last_column, column_before_last,color = 'green', linewidth = 2, label='Second-to-Last Column vs Last Column')

plt.title('Relationship between time and momentum(match 1701)')
plt.xlabel('time(seconds)')
plt.ylabel('psychological momentum')
plt.show()


