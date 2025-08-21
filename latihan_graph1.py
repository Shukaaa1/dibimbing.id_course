import pandas as pd
import matplotlib.pyplot as plt

#ini aku import url dari github
url = 'https://raw.githubusercontent.com/sushantag9/Supermarket-Sales-Data-Analysis/master/supermarket_sales%20-%20Sheet1.csv'

#menampilkan data

pd.set_option('display.max_columns', None)  # Show all columns
df= pd.read_csv(url)

#Dibawah ini adalah analisis untuk mencari kota dengan transaksi terbanyak untuk setiap metode pembayaran
#mengambil kolom city dan payment untuk diketahui
payment_city_count = df.groupby(['Payment', 'City']).size().reset_index(name='Count')
#Mencari kota dengan transaksi terbanyak untuk setiap metode pembayaran
dominant_city = payment_city_count.loc[payment_city_count.groupby('Payment')['Count'].idxmax()]

print(dominant_city)

# Plotting the results
plt.bar(dominant_city['Payment'], dominant_city['Count'], color='skyblue')
plt.xticks(rotation=45)
plt.xlabel('Payment')
plt.ylabel('Jumlah Transaksi Tertinggi per Kota')
plt.title('Kota Dominan untuk Setiap Metode Payment')
for i, v in enumerate(dominant_city['City']):
    plt.text(i, dominant_city['Count'].iloc[i], v, ha='center', va='bottom')
plt.tight_layout()
plt.show()
