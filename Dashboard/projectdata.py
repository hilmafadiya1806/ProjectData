import pandas as pd
import numpy as np
import matplotlib.pyplot as  plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

st.title("Olish Store Dashboard")
st.header('E-Commerce Public Data')
st.subheader('Kepuasan Pelanggan Berdasarkan Riview Score')
def plot_rating_chart():
    # Data dummy untuk distribusi rating
    rating_data = {
        'Rating': [5,4,3,2,1],
        'Jumlah': [56910, 19007,8097,3114,11282]  # Jumlah rating untuk setiap skor
    }

     # Membuat DataFrame dari data dummy
    df = pd.DataFrame(rating_data)

    # Mengurutkan DataFrame berdasarkan kolom 'Rating'
    df_sorted = df.sort_values(by='Rating')

    # Menampilkan chart menggunakan Matplotlib
    fig, ax = plt.subplots()
    ax.bar(df_sorted['Rating'], df_sorted['Jumlah'], color='skyblue')

    # Menambahkan caption jumlah data di atas setiap bar
    for i, v in enumerate(df_sorted['Jumlah']):
        ax.text(i + 1, v + 10, str(v), ha='center', va='bottom')

    ax.set_xlabel('Rating')
    ax.set_ylabel('Jumlah')
    ax.set_title('Riview Kepuasan Pelanggan Berdasarkan Review Score')
    
    # Menampilkan chart menggunakan st.pyplot()
    st.pyplot(fig)

plot_rating_chart()
# Memanggil fungsi untuk menampilkan chart


with st.expander("See explanation"):
    st.write(
        """Berdasarkan grafik diatas menunjukkan bahwa pelanggan sangat puas dengan layanan e-coomerce. Hal tersebut terbukti dengan jumlah pelanggan yang memberikan rating 5 tertinggi dibandingkan dengan rating lainnya.
        """
    )

st.subheader("Persebaran Lokasi Pelanggan")
def plot_seller_distribution():
    seller_data = {
        'Seller_State': ['SP', 'RJ', 'MG', 'RS', 'SC'],
        'Jumlah_Seller': [41746,12852,11635,5466,5045]  # Jumlah penjual untuk setiap negara bagian
    }
    df = pd.DataFrame(seller_data)
    df_sorted = df.sort_values(by='Jumlah_Seller', ascending=False)
    fig, ax = plt.subplots()
    ax.bar(df_sorted['Seller_State'], df_sorted['Jumlah_Seller'], color='skyblue')
    for i, v in enumerate(df_sorted['Jumlah_Seller']):
        ax.text(i, v + 10, str(v), ha='center', va='bottom')

    ax.set_xlabel('Customer State')
    ax.set_ylabel('Number of Customers')
    ax.set_title('Customer Distribution by State')
    st.pyplot(fig)

plot_seller_distribution()
with st.expander("See explanation"):
    st.write(
        """Berdasarkan grafik diatas dapat disimpulkan daerah dengan pelanggan terbanyak yaitu daerah SP dengan jumlah 41746 pelanggan."""
    )
st.subheader("Persebaran Lokasi Penjual")
def plot_seller_distribution():
    seller_data = {
        'Seller_State': ['SP', 'PR', 'MG', 'SC', 'RJ'],
        'Jumlah_Seller': [1849,349,244,190,171] 
    }
    df = pd.DataFrame(seller_data)
    df_sorted = df.sort_values(by='Jumlah_Seller', ascending=False)
    fig, ax = plt.subplots()
    ax.bar(df_sorted['Seller_State'], df_sorted['Jumlah_Seller'], color='skyblue')
    for i, v in enumerate(df_sorted['Jumlah_Seller']):
        ax.text(i, v + 10, str(v), ha='center', va='bottom')

    ax.set_xlabel('Seller State')
    ax.set_ylabel('Number of Sellers')
    ax.set_title('Seller Distribution by State')
    st.pyplot(fig)

plot_seller_distribution()
with st.expander("See explanation"):
    st.write(
        """Berdasarkan grafik diatas dapat disimpulkan persebaran data penjual terbanyak di daerah SP dengan jumlah 1849 penjual."""
    )
st.subheader('Kesimpulan')
st.write(
        """Dengan demikian dapat disimpulkan bahwa pelanggan sangat puas dengan pelayanan e-commerse. Disisi lain, daerah persebaran terbesar pelanggan maupun penjual pada daerah yang sama yaitu SP. Oleh karena itu, untuk meningkatkan kepuasan pelanggan kedepannya dapat dilakukan penyebaran daerah penjual agar daerah pelanggan juga lebih tersebar didaeran lain."""
)
