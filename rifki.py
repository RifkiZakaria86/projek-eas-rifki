import streamlit as st
import numpy as np
from scipy.stats import chi2


def chi_square_test(data, expected_var):
    observed_var = np.var(data)
    n = len(data)
    dof = n - 1  # Derajat kebebasan

    # Hitung statistik uji chi-square
    chi2_stat = (n - 1) * observed_var / expected_var

    # Hitung p-value
    p_value = 1 - chi2.cdf(chi2_stat, dof)

    return observed_var, chi2_stat, p_value


# Tampilan Streamlit
st.title("Uji Chi-Square untuk Varians")
st.write("Uji Chi-Square untuk menentukan apakah varians = 0.5")

# Masukkan data
data = st.text_input(
    "Masukkan data (pisahkan dengan koma)",
    "46.4, 46.1, 45.8, 47, 46.1, 45.9, 45.8, 46.9, 45.2, 46",
)

# Ubah data menjadi array numerik
data = np.array([float(x.strip()) for x in data.split(",")])

# Varians yang diharapkan
expected_var = 0.5

# Lakukan uji chi-square
observed_var, chi2_stat, p_value = chi_square_test(data, expected_var)

# Tampilkan hasil
st.write("Data:", data)
st.write("Hipotesis")
st.write("H0: Varians sama dengan", expected_var)
st.write("H1: Varians tidak sama dengan", expected_var)
st.write("Statistik uji Chi-Square:", chi2_stat)
st.write("P-value:", p_value)

# Interpretasi hasil
alpha = 0.05  # Ambil tingkat signifikansi alpha = 0.05

st.write("\n**Interpretasi Hasil**:")
if p_value < alpha:
    st.write(
        "Keputusan: H0 ditolak karena p-value ({:.4f}) lebih kecil dari alpha ({:.2f}).".format(
            p_value, alpha
        )
    )
    st.write(
        "Berdasarkan hasil uji Chi-Square, ada bukti yang cukup untuk menolak hipotesis nol."
    )
    st.write(
        "Sehingga kesimpulan yang dapat diambil adalah varians data sama dengan 0.5"
    )
else:
    st.write(
        "Keputusan: H0 gagal ditolak karena p-value ({:.4f}) lebih besar dari alpha ({:.2f}).".format(
            p_value, alpha
        )
    )
    st.write(
        "Berdasarkan hasil uji Chi-Square, tidak ada bukti yang cukup untuk menolak hipotesis nol."
    )
    st.write(
        "Sehingga kesimpulan yang dapat diambil adalah varians data tidak sama dengan 0.5."
    )
