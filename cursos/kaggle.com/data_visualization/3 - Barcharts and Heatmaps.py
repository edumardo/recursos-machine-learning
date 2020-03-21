# Setup

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")

# Load the data

flight_filepath = "../input/flight_delays.csv"
flight_data = pd.read_csv(flight_filepath, index_col="Month")

# Bar chart

plt.figure(figsize=(10,6))
plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")
plt.ylabel("Arrival delay (in minutes)")
sns.barplot(x=flight_data.index, y=flight_data['NK'])   # Bar chart showing average arrival delay for Spirit Airlines flights by month
                                                        # x: we select the column that indexes the rows.
                                                        # y: data that will be used to determine the height of each bar

# Heatmap

plt.figure(figsize=(14,7))
plt.title("Average Arrival Delay for Each Airline, by Month")
plt.xlabel("Airline")
sns.heatmap(data=flight_data, annot=True)               # annot: This ensures that the values for each cell appear on the chart
