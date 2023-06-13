import streamlit as st 
import pandas as pd 
import numpy as np 
import seaborn as sns 

# now let start to make demo page 

st.title("EDA ANALAYSIS")

st.subheader("DATA ANALYSIS USING PYTHON AND STREAMLIT")


upload= st.file_uploader("UPLOAD YOUR DATASET IN CSV FORMAT")

if upload is not None:
    data = pd.read_csv(upload)
    
#2 Show data set
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("First 10 data"):
            st.write(data.head(10))
        if st.button("LAST 10 DATASET"):
            st.write(data.tail(10))
        
#3 check datatype of each column    
if upload is not None:
    if st.checkbox("LEARN ABOUT DATATYPES OF ALL THE COLUMNS"):
        st.text("DATATYPES")
        st.write(data.dtypes)
    
# number of not columns and rows in the column:

if upload is not None :
    if st.checkbox(" Check Number of Rows & Columns in your dataset?"):
        data_shape = st.radio("what dimension do you want to check", ("ROWS", "COLUMNS"))
        
        if data_shape == 'ROWS':
            st.text("NUMBER OF ROWS")
            st.write(data.shape[0])
        if data_shape == "COLUMNS":
            st.text("NUMBER OF COLUMNS")
            st.write(data.shape[1])
            
if upload is not None:
    if st.checkbox("CHECK FOR THE NULL VALUES IN DATASET"):
        test = data.isnull().values.any()
        if test == True:
            if st.checkbox("null values in the dataset"):
                
                st.set_option('deprecation.showPyplotGlobalUse', False)
                sns.heatmap(data.isnull())
                st.pyplot()
                st.text(data.isnull().sum())
        else :
            st.text("there are no missing values")


# for the duplicate values 
if upload is not None : 
    if st.checkbox("Do you want to check for duplicate values"):
        test = data.duplicated().any()
        if test == True :
            st.warning("This dataset contains the duplicate values")
            dup  = st.selectbox("Do you want to Rmeove Duplicate Values", ("Select one", "SEE","Yes", "No"))
            if dup == "Yes":
                data = data.drop_duplicates()
                st.text("Duplicates have been removed")
            if dup == "No":
                st.text ("ok No problem")
            if dup == "SEE":
                st.write(data[data.duplicated(keep = False)])
        else : 
            st.text("there are no duplicate columns")
# Get Overall statistics for the user   

if upload is not None:
    if st.checkbox("SUMMARY STATISTICS OF THE DATASET"):
        st.write(data.describe(include= 'all'))

# Get Correlation HeatMap 
if upload is not None : 
    check = st.selectbox("Do you want to see the correlations between Columns?",("Select one","YES", "NO"))
    if check == "YES":
        st.set_option('deprecation.showPyplotGlobalUse', False)
        sns.heatmap(data.corr(method = 'pearson',numeric_only=True), cmap = "YlGnBu", annot = True)
        st.pyplot()
        st.write(data.corr(method = 'pearson',numeric_only=True))
    if check == "NO":
        st.text("You selected not check the correlation")


if upload is not None : 
    value = st.selectbox("Would like to see the distribution of the dataset??", ("select one", "Yes", "No"))
    if value == "Yes":
        new = data.select_dtypes(exclude= "object")
        for i in new.columns:
            st.set_option('deprecation.showPyplotGlobalUse', False)
            sns.distplot(new[i])
            st.pyplot()
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
