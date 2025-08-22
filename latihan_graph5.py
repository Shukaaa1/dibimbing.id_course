import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/sushantag9/Supermarket-Sales-Data-Analysis/master/supermarket_sales%20-%20Sheet1.csv'
df = pd.read_csv(url)

# Kelompokkan data per kota dan produk, jumlahkan total penjualan
city_product_sales = df.groupby(['City', 'Product line'])['Total'].sum().reset_index()

# Gunakan palette seaborn sesuai jumlah produk
product_lines = city_product_sales['Product line'].unique()
palette = sns.color_palette("tab10", len(product_lines))

plt.figure(figsize=(12,6))
ax = sns.barplot(
    x='City', y='Total', hue='Product line', data=city_product_sales,
    dodge=True, palette=palette
)
plt.title('Total Penjualan Setiap Produk di Setiap Kota')
plt.xlabel('Kota')
plt.ylabel('Total Sales')
plt.tight_layout()

# Tambahkan outline pada setiap bar
for p in ax.patches:
    p.set_edgecolor('black')
    p.set_linewidth(1.5)
    if p.get_height() > 0:
        ax.text(
            p.get_x() + p.get_width()/2,
            p.get_height() + 50,
            f"{int(p.get_height())}",
            ha='center', va='bottom', fontsize=9
        )

plt.legend(title='Product Line', loc='upper right')
plt.show()