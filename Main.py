from LogisticRegression import *
from ReadProcess import *
from ContentsOfCSVFile import *
import streamlit as st




def main_page():
    st.title("**Loan Eligibility 💵**")
    # Create a checkbox
    Toggle = st.toggle("Toggle For Filling Form/Visualization Of Chart")

    if Toggle == False: 
        interface()
    else:
        chart()


def page2():
    st.title("**Dataset Presented Below 📈**")
    st.sidebar.markdown("**Contents Of CSV 📋**")
    ShowData(DataSet)
    
    

page_names_to_funcs = {
    "Loan Eligibility 💲": main_page,
    "Contents Of Original CSV File": page2
}

selected_page = st.sidebar.selectbox("**Select Dropdown Options**", page_names_to_funcs.keys())

page_names_to_funcs[selected_page]()