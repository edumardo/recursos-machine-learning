# Setup

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")

# Load the data

spotify_filepath = "../input/spotify.csv"
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)

# Plot the data

plt.figure(figsize=(14,6))                                              # Set the width and height of the figure
plt.title("Daily Global Streams of Popular Songs in 2017-2018")         # Add title
sns.lineplot(data=spotify_data)                                         # Line chart

# Plot a subset of the data

list(spotify_data.columns)                                              # Names of all columns of the data
plt.figure(figsize=(14,6))                                              # Width and height of the figure
plt.title("Daily Global Streams of Popular Songs in 2017-2018")         # Title
sns.lineplot(data=spotify_data['Shape of You'], label="Shape of You")   # Line chart showing only 'Shape of You'
sns.lineplot(data=spotify_data['Despacito'], label="Despacito")         # Line chart showing only 'Despacito'
plt.xlabel("Date")                                                      # Add label for horizontal axis
