import streamlit as st
import pandas as pd

st.title('B.M.I CALULATOR')

height = st.slider("enter your height in cm", 100, 250, 175)
weight = st.slider("enter your weight in kg", 40, 200, 70)