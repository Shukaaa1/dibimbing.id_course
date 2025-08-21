import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

url2 = 'https://raw.githubusercontent.com/sushantag9/Supermarket-Sales-Data-Analysis/master/supermarket_sales%20-%20Sheet1.csv'
df2 = pd.read_csv(url2)

#kita akan menampilkan jumlah penjualan per produk
# Menyiapkan data agregat
sales_per_product = df2.groupby('Product line')['Total'].sum().reset_index()

# Membuat list warna: hijau untuk tertinggi, biru untuk lainnya
colors = ['blue'] * len(sales_per_product)
max_idx = sales_per_product['Total'].idxmax()
colors[max_idx] = 'green'

plt.figure(figsize=(10, 6))
ax = sns.barplot(x='Product line', y='Total', data=sales_per_product, ci=None, palette=colors)

plt.title('Total Sales by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()

for i, row in sales_per_product.iterrows():
    ax.text(i, row['Total'] + 5, f"{row['Total']:.0f}", ha='center', va='bottom', fontsize=10)

plt.show()