import streamlit as st

st.title('PENGKATEGORIAN pH')

nilai = st.number_input("Masukkan Nilai pH = ", 0)
hasil = st.button("Hasil pH")

if 11<=nilai<14:
    st.write("BASA KUAT", hasil)
    st.write("Warna Violet", hasil)
elif 9<=nilai<10:
    st.write("BASA LEMAH", hasil)
    st.write("Warna Ungu", hasil)
elif nilai==8:
    st.write("BASA SANGAT LEMAH", hasil)
    st.write("Warna Biru", hasil)
elif nilai==7:
    st.write("NETRAL", hasil)
    st.write("Warna Hijau", hasil)
elif nilai==6:
    st.write("ASAM SANGAT LEMAH", hasil)
    st.write("Warna Kuning", hasil)
elif 4<=nilai<5:
    st.write("ASAM LEMAH", hasil)
    st.write("Warna Orange", hasil)
elif 1<=nilai<3:
    st.write("ASAM KUAT", hasil)
    st.write("Warna Merah", hasil)
else:
    st.write("BATASE MUNG TEKAN 14 COKK", hasil)