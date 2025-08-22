import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/sushantag9/Supermarket-Sales-Data-Analysis/master/supermarket_sales%20-%20Sheet1.csv'
df = pd.read_csv(url)

# Kelompokkan data per kota dan produk, jumlahkan total penjualan
city_product_sales = df.groupby(['City', 'Product line'])['Total'].sum().reset_index()

# Ambil produk dengan penjualan tertinggi di setiap kota
idx = city_product_sales.groupby('City')['Total'].idxmax()
top_products = city_product_sales.loc[idx].reset_index(drop=True)

# Plot barplot
plt.figure(figsize=(8,6))
ax = sns.barplot(x='City', y='Total', hue='Product line', data=top_products)
plt.title('Produk dengan Penjualan Tertinggi di Setiap Kota')
plt.xlabel('Kota')
plt.ylabel('Total Sales')
plt.legend(title='Product Line')
plt.tight_layout()

for i, row in top_products.iterrows():
    ax.text(
        i, row['Total'] + 50, f"{row['Total']:.0f}",
        ha='center', va='bottom', fontsize=10
    )

plt.show()