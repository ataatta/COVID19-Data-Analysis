import pandas as pd

# Load the data
file_path = 'COVID19.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the data
print(data.head())

# Display basic information about the data
print(data.info())

# Display summary statistics
print(data.describe())

# Check for missing values
print(data.isnull().sum())

# Fill or drop missing values as necessary (example: fill with zero)
data = data.fillna(0)

# Verify changes
print(data.info())

# Calculate mean, median, and mode for cumulative cases
cumulative_cases_mean = data['Cases - cumulative total'].mean()
cumulative_cases_median = data['Cases - cumulative total'].median()
cumulative_cases_mode = data['Cases - cumulative total'].mode()[0]

# Calculate mean, median, and mode for cumulative deaths
cumulative_deaths_mean = data['Deaths - cumulative total'].mean()
cumulative_deaths_median = data['Deaths - cumulative total'].median()
cumulative_deaths_mode = data['Deaths - cumulative total'].mode()[0]

# Display results
print(f"Cumulative Cases - Mean: {cumulative_cases_mean}, Median: {cumulative_cases_median}, Mode: {cumulative_cases_mode}")
print(f"Cumulative Deaths - Mean: {cumulative_deaths_mean}, Median: {cumulative_deaths_median}, Mode: {cumulative_deaths_mode}")

#creating a plot
import matplotlib.pyplot as plt
import seaborn as sns

# Plotting cumulative cases
plt.figure(figsize=(10, 6))
sns.histplot(data['Cases - cumulative total'], kde=True)
plt.title('Distribution of Cumulative COVID-19 Cases')
plt.xlabel('Cumulative Cases')
plt.ylabel('Frequency')
plt.show()

# Plotting cumulative deaths
plt.figure(figsize=(10, 6))
sns.histplot(data['Deaths - cumulative total'], kde=True)
plt.title('Distribution of Cumulative COVID-19 Deaths')
plt.xlabel('Cumulative Deaths')
plt.ylabel('Frequency')
plt.show()

# Example: Rolling average for new cases reported in last 7 days
data['new_cases_rolling'] = data['Cases - newly reported in last 7 days'].rolling(window=7).mean()

# Plotting the rolling average
plt.figure(figsize=(10, 6))
sns.lineplot(x=data.index, y='new_cases_rolling', data=data)
plt.title('7-Day Rolling Average of Newly Reported COVID-19 Cases')
plt.xlabel('Index')
plt.ylabel('New Cases (7-Day Rolling Average)')
plt.show()
