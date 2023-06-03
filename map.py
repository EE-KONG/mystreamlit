import streamlit as st
import pandas as pd
import numpy as np

df=pd.DataFrame((np.random.randn(500,2)/[10,10])+[37.34,126.58],columns=['lat','lon'])
st.map(df)
