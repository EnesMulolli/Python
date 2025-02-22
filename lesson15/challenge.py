import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read CSV file
df = pd.read_csv('weather_tokyo_data.csv')

# Step 2: Monthly Average Temperature Plot
avg_temperature = df.groupby('Month')['temperature'].mean()

plt.figure(figsize=(13, 8))
avg_temperature.plot(marker='o', color='skyblue')

plt.title('Monthly Average Temperature in Tokyo')
plt.xlabel('Month')
plt.ylabel('temperature')

plt.grid(linestyle='--', alpha=0.7)
plt.show()

# Step 3: Hottest and Coldest Day
hottest_day = df[df['temperature'] == df['temperature'].max()]
coldest_day = df[df['temperature'] == df['temperature'].min()]

print("Hottest Day:\n", hottest_day)
print("Coldest Day:\n", coldest_day)

# Step 4: Temperature Over Time Plot
plt.figure(figsize=(13.8))
plt.plot(df.index, df['temperature'], marker='o', color='SkyBlue', linestyle='-')
plt.title('Temperature Over Time')
plt.xlabel('Time (Index)')
plt.ylabel('Temperature')
plt.grid(linestyle='--', alpha=0.7)
plt.show()

# Step 5: Calculate Seasons and Plot Seasonal Averages
df['Season'] = (df['Month'] - 1) // 3 + 1  # Fix the season calculation
seasonal_avg = df.groupby('Season')['temperature'].mean()

plt.figure(figsize=(10, 6))
seasonal_avg.plot(kind='bar', color='orange')
plt.title('Seasonal Average Temperature in Tokyo')
plt.xlabel('Season')
plt.ylabel('temperature')
plt.xticks([0, 1, 2, 3], ['Winter', 'Spring', 'Summer', 'Fall'])

plt.grid(linestyle='--', alpha=0.7)
plt.show()
