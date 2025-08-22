import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/sushantag9/Supermarket-Sales-Data-Analysis/master/supermarket_sales%20-%20Sheet1.csv'
df = pd.read_csv(url)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/sushantag9/Supermarket-Sales-Data-Analysis/master/supermarket_sales%20-%20Sheet1.csv'
df = pd.read_csv(url)

# Ubah kolom Date ke datetime
df['Date'] = pd.to_datetime(df['Date'])

# Tambahkan kolom week (minggu ke berapa dalam tahun)
df['Week'] = df['Date'].dt.isocalendar().week

# Kelompokkan dan jumlahkan total penjualan per minggu
weekly_sales = df.groupby('Week')['Total'].sum().reset_index()

# Plot line chart
plt.figure(figsize=(10,6))
sns.lineplot(x='Week', y='Total', data=weekly_sales, marker='o')
plt.title('Total Penjualan per Minggu')
plt.xlabel('Minggu')
plt.ylabel('Total Penjualan')
plt.tight_layout()

max_idx = weekly_sales['Total'].idxmax()
min_idx = weekly_sales['Total'].idxmin()

max_row = weekly_sales.iloc[max_idx]
min_row = weekly_sales.iloc[min_idx]

plt.text(max_row['Week'], max_row['Total']+500, f"{max_row['Total']:.0f}", 
         ha='center', va='bottom', color='green', fontsize=11, fontweight='bold')
plt.text(min_row['Week'], min_row['Total']-500, f"{min_row['Total']:.0f}", 
         ha='center', va='top', color='red', fontsize=11, fontweight='bold')

plt.show()
