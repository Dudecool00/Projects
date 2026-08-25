import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt
import seaborn as sns

# Read the two CSV files
df1 = pd.read_csv('2024_Season.csv')  # 2024 season data
df2 = pd.read_csv('2014_Season.csv')  # 2014 season data

# Clean the data - remove commas from YDS and convert to float
df1['YDS'] = df1['YDS'].str.replace(',', '').astype(float)
df2['YDS'] = df2['YDS'].str.replace(',', '').astype(float)

# Ensure CMP% and AVG are float
df1['CMP%'] = df1['CMP%'].astype(float)
df2['CMP%'] = df2['CMP%'].astype(float)
df1['AVG'] = df1['AVG'].astype(float)
df2['AVG'] = df2['AVG'].astype(float)

# Create combined DataFrame
combined_df = pd.DataFrame({
    'Season': ['2024'] * len(df1) + ['2014'] * len(df2),
    'CMP%': df1['CMP%'].tolist() + df2['CMP%'].tolist(),
    'AVG': df1['AVG'].tolist() + df2['AVG'].tolist()
})

# Create scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=combined_df, x='CMP%', y='AVG', hue='Season', palette={'2014': 'red', '2024': 'blue'})

# Add lines of best fit
sns.regplot(data=combined_df[combined_df['Season'] == '2024'], x='CMP%', y='AVG', scatter=False, color='blue', line_kws={'label': '2024 Best Fit'})
sns.regplot(data=combined_df[combined_df['Season'] == '2014'], x='CMP%', y='AVG', scatter=False, color='red', line_kws={'label': '2014 Best Fit'})

plt.title('Scatterplot of CMP% vs AVG by Season')
plt.legend()
plt.tight_layout()
plt.savefig('scatterplot_cmp_avg.png')