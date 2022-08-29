import streamlit as st
import pandas as pd

#define data
d = pd.read_csv("distinct.tsv", sep="\t")


#create sidebar input
with st.sidebar:
    a = st.text_input("属名", value="")
    b = st.text_input("種名", value="")

df = d[d['F'].str.contains(a)]
df = df[df['G'].str.contains(b)]

st.dataframe(df)

st.text(f"{df.shape[0]}件のヒット")