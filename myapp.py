import streamlit as st

x=st.slider("WoW",10,50)
b=st.button("버튼을 누르세요.")
if b==True:
  if x<20: st.write("C")
  elif x<40: st.write("B")
  else: st.write("A")
