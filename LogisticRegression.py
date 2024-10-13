from sklearn.linear_model import LinearRegression
from sklearn import metrics
from ReadProcess import DataSet
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from LoanStatus import *
import joblib 


def TrainTestSplit():

    
    
    X = DataSet.drop('Credit_History', axis=1)
    y = DataSet['Credit_History']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=45)

    print(f"The shape of X_train: \n{X_train.shape}")
    print(f"The shape of X_train: \n{X_train.shape}")


    ML_Model(X_train, X_test, y_train, y_test)


def ML_Model(X_train, X_test, y_train, y_test):
    
    model = LogisticRegression()

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print(f"The predicted value of X_test: {y_pred}")

    print(f"The accuracy between Prediction and Real Value: {metrics.accuracy_score(y_pred, y_test)}")
    print(f"The F1 score between Prediction and Real Value: {metrics.f1_score(y_pred, y_test)}")
    joblib.dump(model,'model.pkl') # Saving the model as model.pkl
    

def finalPrediction(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Property_Area):
    
    model = joblib.load("model.pkl")
    
    finalRes = (Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Property_Area)

        #chaning it to numpy array
    input_data_as_array = np.asarray(finalRes)

    #reshapping the data
    input_data_reshaped = input_data_as_array.reshape(1,-1)


    prediction = model.predict(input_data_reshaped)
    
    if int(prediction[0]) == 1:
        print("Loan Is Approval 😎")
        return LoanApproved()
        
    else:
        print("Loan Not Approved 😔")
        return loanNotApproved()
        

def interface():

    with st.form(key = "form1"):

    # Gender,Married,Dependents,Education,Self_Employed,
    
        Gender = st.selectbox("**Select Gender: -**", ("Male", "Female"))
        st.write(f"**Gender selected: {Gender}**")
        
        if(Gender == 'Male'):
            Gender = 1
        else:
            Gender = 2

        st.markdown("\n")

        
        Married = st.selectbox("**Marriage Status: -**", ("Yes", "No"))
        st.write(f"**Status selected: {Married}**")
        
        if(Married == 'Yes'):
            Married = 1
        else:
            Married = 2

        st.markdown("\n")

        Dependents = st.number_input("**Enter Number Of Children: -**", min_value=0, max_value=5, label_visibility="visible")
        st.write(f"**Number Of Children: {Dependents}**")

        st.markdown("\n")

        
        Education = st.selectbox("**Education Status: -**", ("Graduate", "Not Graduate"))
        st.write(f"**Education selected: {Education}**")
        
        if(Education == 'Graduate'):
            Education = 1
        else:
            Education = 2

        st.markdown("\n")

        Employment = st.selectbox("**Employment Status: -**", ("Yes", "No"))
        st.write(f"**Employment selected: {Employment}**")
        
        if(Employment == 'Yes'):
            Employment = 1
        else:
            Employment = 2

        st.markdown("\n")

        # ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area
        AppIncome = st.number_input("**Enter Applicant's Income: -**", min_value=0, max_value=40000, label_visibility="visible")
        st.write(f"**Applicant's Income: ${AppIncome}**")

        st.markdown("\n")

        
        CoApplicant = st.number_input("**Enter CoApplicant's Income: -**", min_value=0, max_value=40000, label_visibility="visible")
        st.write(f"**CoApplicant's Income: ${CoApplicant}**")

        st.markdown("\n")

        
        
        loanAmount = st.number_input("**Enter Loan Amount: -**", min_value=0.00, max_value=1000.00, label_visibility="visible")
        st.write(f"**Loan Amount: ${loanAmount}**")

        st.markdown("\n")
        
        loanTerm = st.number_input("**Enter Loan Period: -**", min_value=10.00, max_value=360.00, label_visibility="visible")
        st.write(f"**Loan Period: {loanTerm} days**")

        st.markdown("\n")

        Property = st.selectbox("**Location Status: -**", ("Rural", "Semiurban", "Urban"))
        st.write(f"**Location selected: {Property}**")
        
        if(Property == 'Rural'):
            Property = 1
        elif(Property == 'Semiurban'):
            Property = 2
        else:
            Property = 3

        st.markdown("\n")

        
        

        # Create a Submit button
        if st.form_submit_button("**Submit Form**", type='primary' ,use_container_width=True):
            
            result =  finalPrediction(Gender, Married, Dependents, Education, Employment, AppIncome, CoApplicant, loanAmount, loanTerm, Property)
        
        else:
            result = ""  # Initialize result as an empty string

        # Display the result below the button
        st.write(result)







def chart():

    # st.line_chart(DataSet['LoanAmount'])
    st.markdown('\n')
    st.markdown('\n')
    chart_data = pd.DataFrame(
        {
            "Loan Amount": DataSet['LoanAmount'],
            "Loan Period": DataSet['Loan_Amount_Term']
        }
    )
    st.subheader("**Bar Chart [ Loan Amount Vs Loan Period ]**")
    st.markdown('\n')
    

    st.bar_chart(chart_data, x="Loan Amount", y="Loan Period", color='#fe4a49', use_container_width=True)

    # st.markdown("**The above bar chart shows the loan amount used per person w.r.t the loan period for the same.**")
    st.markdown('\n')
    st.markdown('\n')
    st.markdown('\n')
    st.markdown('\n')
    DSA = pd.read_csv('LoanPrediction copy.csv')

    DSA_Filter = DSA.dropna()

    chart_data2 = pd.DataFrame(
        {
            "Gender": DSA_Filter['Gender'],
            "Loan Amount": DSA_Filter['LoanAmount'],
            "Approval Ratings": DSA_Filter['Credit_History']
        }
    )
    st.subheader("**Bar Chart [ Gender Vs Approval Ratings ]**")
    st.bar_chart(chart_data2, x="Gender", y="Approval Ratings")

    print(DSA_Filter["Credit_History"].value_counts())

TrainTestSplit()