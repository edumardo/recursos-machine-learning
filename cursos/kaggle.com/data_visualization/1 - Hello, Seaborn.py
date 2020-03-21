# Setup

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")

# Load the data

fifa_filepath = "../input/fifa.csv"                                         # index_col: we want each entry in the first column to denote a different row
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)  # parse_dates: tells the notebook to understand the each row label as a date

# Plot the data

plt.figure(figsize=(16,6))      # Set the width and height of the figure
sns.lineplot(data=fifa_data)    # Line chart showing how FIFA rankings evolved over time
