import streamlit as st
import pandas as pd
import numpy as np

df=pd.DataFrame((np.random.randn(500,2)/[10,10])+[37.20,126.44]+[37.48,126.72],columns=['lat','lon'])
st.map(df)
