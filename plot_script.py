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

# YDS/G and QBR are already float, but ensure
df1['YDS/G'] = df1['YDS/G'].astype(float)
df2['YDS/G'] = df2['YDS/G'].astype(float)

df1['QBR'] = df1['QBR'].astype(float)
df2['QBR'] = df2['QBR'].astype(float)

# Reshape data into long format
qbr_df = pd.DataFrame({
    'Season': ['2024'] * len(df1) + ['2014'] * len(df2),
    'QBR': df1['QBR'].tolist() + df2['QBR'].tolist()
})

ydsg_df = pd.DataFrame({
    'Season': ['2024'] * len(df1) + ['2014'] * len(df2),
    'YDS/G': df1['YDS/G'].tolist() + df2['YDS/G'].tolist()
})

# Create side-by-side box plots
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Box plot for QBR
sns.boxplot(data=qbr_df, x='Season', y='QBR', ax=axes[0])
axes[0].set_title('QBR Comparison')

# Box plot for YDS/G
sns.boxplot(data=ydsg_df, x='Season', y='YDS/G', ax=axes[1])
axes[1].set_title('YDS/G Comparison')

plt.tight_layout()
plt.savefig('box_plots_qbr_ydsg.png')