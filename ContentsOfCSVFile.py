import streamlit as st
import pandas as pd

def ShowData(DSA):

    DSA = pd.read_csv('LoanPrediction copy.csv')
    DSA_Filter = DSA.dropna(inplace=True)
    st.write(DSA)
    # st.write("⚝──────────⭒─────⭑─────⭒──────────────⭒─────⭑─────⭒──────────⚝")
    # st.subheader("**The data is as below: -**")
    # st.write("**Male: 1 && Female: 2**")
    # st.write("**Marriages[Yes]: 1 && Marriage[No]: 2**")
    # st.write("**Graduate: 1 && Not Graduate: 2**")
    # st.write("**Employment[Yes]: 1 && Employment[No]: 2**")
    # st.write("**Property[Rural]: 1 && Property[SemiUrban]: 2 && Property[Urban]: 3**")
    # st.write("⚝──────────⭒─────⭑─────⭒──────────────⭒─────⭑─────⭒──────────⚝")