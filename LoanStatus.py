import streamlit as st

def LoanApproved():

    st.markdown(
    """
    <style>
        
        .highlight {
            font-family: 'Roboto', sans-serif;
            font-size: 45px;
            line-height: 2;
            font-weight: bold;
            justify-content: center; /* Horizontally centers */
            align-items: center; /* Vertically centers */
            text-align: center;
            border: 3px solid #3498db;
            border-radius: 15px; /* Rounded corners */  
            background-color: red; 
            color: #87CEFA;
        }

        body{
            background-color: #333; /* Black eyes */
        }
    </style>
    """,
    unsafe_allow_html=True,
    )
    
    st.markdown('<h1 class="highlight">Loan Approved 🤝</h1><br>', unsafe_allow_html=True)

def loanNotApproved():
    st.markdown(
    """
    <style>
        
        .highlight {
            font-family: 'Roboto', sans-serif;
            font-size: 45px;
            line-height: 2;
            font-weight: bold;
            justify-content: center; /* Horizontally centers */
            align-items: center; /* Vertically centers */
            text-align: center;
            border: 3px solid #3498db;
            border-radius: 15px; /* Rounded corners */  
            background-color: #87CEFA; 
            color: red;
            border: 10px solid #228B22; /* Adjust the pixel value for thickness */
        }

        body{
            background-color: #333; /* Black eyes */
        }
    </style>
    """,
    unsafe_allow_html=True,
    )
    
    st.markdown('<h1 class="highlight">Loan Application Denied 🏛️</h1><br>', unsafe_allow_html=True)

