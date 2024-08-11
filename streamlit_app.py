import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.info('This is app builds a machine learning model!')

df = pd.read_csv("https://github.com/dataprofessor/data/blob/c2b6c1fb592c9d7a07e6a08a5bf417209f4b1400/penguins_cleaned.csv")
df


