import streamlit as st
import sklearn
import plotly 
st.title("GIAI PHUONG TRINH BAC NHAT")
a = st.number_input('Tham so a')
b = st.number_input('Tham so b')
if st.button('Giai'):
  st.write('Phuong trinh co 1 nghiem ', -b/a)
