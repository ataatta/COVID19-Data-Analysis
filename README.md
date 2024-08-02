# COVID19-Data-Analysis
A comprehensive analysis of COVID-19 data, including descriptive statistics, data visualizations, and advanced analysis techniques. This project showcases skills in data cleaning, exploration, and visualization using Python.

# COVID-19 Data Analysis Project

## Project Description
This project analyzes COVID-19 data from an Excel sheet. The analysis includes calculating descriptive statistics such as mean, median, and mode for cases and deaths. Additionally, it features data visualizations and advanced analyses like rolling averages to identify trends over time.

## Data
The data used in this project contains the following columns:
- Name
- WHO Region
- Cases - cumulative total
- Cases - cumulative total per 100000 population
- Cases - newly reported in last 7 days
- Cases - newly reported in last 7 days per 100000 population
- Cases - newly reported in last 24 hours
- Deaths - cumulative total
- Deaths - cumulative total per 100000 population
- Deaths - newly reported in last 7 days
- Deaths - newly reported in last 7 days per 100000 population
- Deaths - newly reported in last 24 hours

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/COVID19-Data-Analysis.git
   cd COVID19-Data-Analysis

2. Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3.  Install the necessary libraries:
pip install pandas numpy matplotlib seaborn

4. Run the analysis script:
python analysis.py

Data Exploration
The initial step involves loading the data and understanding its structure. The data is loaded using pandas, and basic information about the dataset is displayed.
import pandas as pd

# Load the data
file_path = 'COVID19.csv'
data = pd.read_csv(file_path)

# Display basic information about the data
print(data.info())

# Display summary statistics
print(data.describe())

Data Cleaning
Missing values are handled by filling them with zeros. Data types are also checked and corrected if necessary.
# Fill or drop missing values as necessary (example: fill with zero)
data = data.fillna(0)

# Verify changes
print(data.info())

Descriptive Statistics
Mean, median, and mode are calculated for cumulative cases and deaths.
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

Data Visualization
Histograms and line plots are created to visualize the distribution and trends of the data.
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

Advanced Analysis
An example of advanced analysis includes calculating and plotting a rolling average for new cases reported in the last 7 days.
# Example: Rolling average for new cases reported in last 7 days
data['new_cases_rolling'] = data['Cases - newly reported in last 7 days'].rolling(window=7).mean()

# Plotting the rolling average
plt.figure(figsize=(10, 6))
sns.lineplot(x=data.index, y='new_cases_rolling', data=data)
plt.title('7-Day Rolling Average of Newly Reported COVID-19 Cases')
plt.xlabel('Index')
plt.ylabel('New Cases (7-Day Rolling Average)')
plt.show()

Conclusion
This project provides a comprehensive analysis of COVID-19 data, including descriptive statistics, data visualizations, and advanced analysis techniques. The code and findings are documented to help others understand and replicate the analysis.


