import streamlit as st
import pandas as pd
import numpy as np

df=pd.DataFrame((np.random.randn(500,2)/[10,10])+[35.2432,128.8812],columns=['lat','lon'])
st.map(df)
df=pd.DataFrame((np.random.randn(500,2)/[50,50])+[35.2432,128.8812],columns=['lat','lon'])
st.map(df)
df=pd.DataFrame((np.random.randn(500,2)/[100,100])+[35.2432,128.8812],columns=['lat','lon'])
st.map(df)
