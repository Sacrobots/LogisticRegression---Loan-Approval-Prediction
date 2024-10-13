import streamlit as st
import pandas as pd
from sklearn import *



global DataSet

DataSet = pd.read_csv('LoanPrediction.csv')


def ReadCheckPreprocess():

    print(f"Top 5 rows: \n{DataSet.head(5)}\n")

    print(f"Number of columns: \n{DataSet.columns}\n")

    print(f"Unique fields in Education: \n", DataSet['Education'].unique(), "\n")
    print(f"Unique fields in Property Area: \n", DataSet['Property_Area'].unique(), "\n")
    print(f"Unique fields in Gender Area: \n", DataSet['Gender'].unique(), "\n")

    
    print("-----------------------------------------------------------------------")

    print(f"Number Of Null Values In Dataset: \n{DataSet.isnull().sum()}\n")

    print(f"Description Of Data Set:\n{DataSet.describe()}\n")

    print("After dropping all null values\n")
    DataSet.dropna(inplace=True)

    print(f"Number Of Null Values In Dataset: \n{DataSet.isnull().sum()}\n")

    print(f"Number of rows: {len(DataSet)}")

    print("Remove uneccessary columns:\n")

    print(DataSet.head())
    Categorical()


def Categorical():

    categorical_cols = [var for var in DataSet.columns if DataSet[var].dtype == 'O']

    print(f"The categorical columns are: {categorical_cols}")

    for i in categorical_cols:

        print(DataSet[i].unique())

    # DataSet.drop('Loan_ID', axis=1, inplace=True)

    # pd.set_option('future.no_silent_downcasting', True)

    DataSet['Gender'].replace({'Male': 1, 'Female': 2}, inplace=True)
    DataSet['Education'].replace({'Graduate': 1, 'Not Graduate': 2}, inplace=True)
    DataSet['Self_Employed'].replace({'No': 2, 'Yes': 1}, inplace=True)
    DataSet['Married'].replace({'No': 2, 'Yes': 1}, inplace=True)
    DataSet['Dependents'].replace({'3+': 3}, inplace=True)
    DataSet['Property_Area'].replace({'Rural': 1, 'Semiurban': 2, 'Urban': 3}, inplace=True)

    DataSet.to_csv('LoanPrediction.csv', index=False)
    
    print(DataSet.head())

def seperateCol():

    print(DataSet['Dependents'].head(20))
