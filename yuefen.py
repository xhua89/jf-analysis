# -*- encoding:utf-8 -*- 
"""
PyCharmzhanshi
2025年03月19日
by hua
"""

import streamlit as st
import pandas as pd

df_yf= pd.read_csv("./result_yf.csv")
st.dataframe(df_yf)
st.divider()
df_yf2= pd.read_csv("./result_ysp.csv")
st.dataframe(df_yf2)
st.divider()