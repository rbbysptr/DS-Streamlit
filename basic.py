import streamlit as st
import pandas as pd
import plotly.express as px

#judul
st.title("Dasar-dasar Streamlit")

#example input
nama = st.text_input("siapa nama kamu? ")
st.write(f"Halo {nama}")

data = {"bulan": ["jan","feb","mar","apr"],
        "penjualan":[10,5,50,25]}

#baca data
df = pd.DataFrame(data)

st.header("data penjualan")

#tampilkan data
st.dataframe(df)

st.subheader("Grafik penjualan line chart")

#mencipatkan visualisasinya
visual_line = px.line(df, x="bulan", y="penjualan", markers=True)

#visualisasinya ditampilkan di streamlit
st.plotly_chart(visual_line)