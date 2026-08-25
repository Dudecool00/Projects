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

# Ensure the columns are float
columns = ['CMP%', 'YDS/G', 'TD', 'INT', 'QBR']
for col in columns:
    df1[col] = df1[col].astype(float)
    df2[col] = df2[col].astype(float)

# Create heatmaps for each season
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# 2024 Season heatmap
corr1 = df1[columns].corr()
sns.heatmap(corr1, annot=True, cmap='coolwarm', ax=axes[0], vmin=-1, vmax=1)
axes[0].set_title('2024 Season Correlation Heatmap')

# 2014 Season heatmap
corr2 = df2[columns].corr()
sns.heatmap(corr2, annot=True, cmap='coolwarm', ax=axes[1], vmin=-1, vmax=1)
axes[1].set_title('2014 Season Correlation Heatmap')

plt.tight_layout()
plt.savefig('heatmaps_cmp_ydsg_td_int_qbr.png')