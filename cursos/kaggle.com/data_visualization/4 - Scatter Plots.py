# Setup

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")

# Load the data

insurance_filepath = "../input/insurance.csv"
insurance_data = pd.read_csv(insurance_filepath)

# Scatter plots

sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])
sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])       # Add a regresion line: line that best fits the data

# Color-coded scatter plots

sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])
    # We can use scatter plots to display the relationships between three variables

sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)     # Two regresion lines

# Categorical scatter plot

sns.swarmplot(x=insurance_data['smoker'], y=insurance_data['charges'])
    # we can adapt the design of the scatter plot to feature a categorical variable (like "smoker") on one of the main axes.
