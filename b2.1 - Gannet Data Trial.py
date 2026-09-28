# importing numpy etc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.plotting.register_matplotlib_converters()
print("Setup Complete")

# Define file path and selected data
GT2_filepath = '../GANNET-05-27-2024-18-30-16-312-gannet-1.csv'
GT2_data = pd.read_csv(GT2_filepath, index_col="No", parse_dates=False)
# index column = "No" i.e. number, parse_dates=false is just telling it not to parse the dates into date format
print(GT2_data.head())
print(GT2_data.tail())

# Graph plot
plt.figure(figsize=(15, 5))
plt.title("GT2 PT Speed Control")
sns.lineplot(data=GT2_data['[EC2]a99ggnh1'], label="N2 Spool Speed")
sns.lineplot(data=GT2_data['[EC2]a99ggnl1'], label="N1 Spool Speed")
sns.lineplot(data=GT2_data['[EC2]a99pt1'], label="PT Spool Speed")
sns.lineplot(data=GT2_data['[EC2]n1set'], label="N1 Set Point")
plt.xlabel("Time (s)")
plt.ylabel("RPM")
plt.show()