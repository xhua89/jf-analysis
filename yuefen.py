# -*- encoding:utf-8 -*- 
"""
PyCharmzhanshi
2025年03月19日
by hua
"""

import streamlit as st
import pandas as pd

df_yf= pd.read_csv("D:\\建发\\result_yf.csv")
st.dataframe(df_yf)
st.divider()
df_yf2= pd.read_csv("D:\\建发\\result_ysp.csv")
st.dataframe(df_yf2)
st.divider()