import streamlit as st 

st.set_page_config(
    page_title = "Matematika Geometri",
    page_icon = "🏆"
)

with st.sidebar:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("geometri.png")
    st.title("Bangun Datar")
    pilihan = st.selectbox("Pilihan Bangun Datar", ["Persegi","Persegi Panjang","Lingkaran"])
    st.caption("Dibuat dengan :fire: oleh **Adi Setiawan**")

match pilihan:
    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung `luas` dan `keliling` persegi")
        sisi = st.number_input("Masukkan Sisi")
        if st.button("Hitung", type="primary"):
            luas = sisi * sisi 
            keliling = 4 * sisi
            # st.success(f"Luas persegi adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2:
                st.metric("Keliling", value=keliling, border=True)
            st.snow()


    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung `luas` dan `keliling` persegi panjang")
        panjang = st.number_input("Masukkan Panjang")
        lebar = st.number_input("Masukkan Lebar")
        if st.button("Hitung", type="primary"):
            luas = panjang * lebar 
            keliling = 2 * (panjang + lebar)
            st.success(f"Luas persegi panjang adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.balloons()

    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung `luas` dan `keliling` lingkaran")
        jarijari = st.number_input("Masukkan Jari-jari")
        if st.button("Hitung", type="primary"):
            luas = 3.14 * jarijari * jarijari
            keliling = 2 * 3.14 * jarijari 
            st.success(f"Luas lingkaran adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.balloons()

    case _ :
        st.error("Terjadi kesalahan")