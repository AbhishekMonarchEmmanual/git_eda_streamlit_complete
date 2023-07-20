import streamlit as st 
import pandas as pd 
import numpy as np 
import seaborn as sns
import scipy as sp 
import os, sys
from trycatch.exception import SystemException 
from trycatch.logger import logging

class data_profile_streamlit:
     
    def __init__(self):
        logging.info("first_page_initiated") 
        if st.button("Terminate App", key="terminate_btn"):
            st.warning("Stopping the Streamlit app...")
            os._exit(0)
        st.title("EDA ANALAYSIS")
        

        st.header("DATA ANALYSIS USING PYTHON AND STREAMLIT")
        
        upload= st.file_uploader("UPLOAD YOUR DATASET IN CSV OR XLSX FORMAT")
      
        try: 
            logging.info("file submitted")

            if upload is not None:
                st.subheader(f'THE FILE {upload.name} is ready for analysis')
                extension = upload.name
                ext = extension.split(".")
                st.warning(f"{ext[-1]} is of this format")
                st.warning(f"file should have .csv or .xlsx in the end")
   
                if ext[-1] == "csv":
                    self.data = pd.read_csv(upload)
                    self.show_dataset(data= self.data)
                    self.check_data(data=self.data)
                    self.no_of_col_row(data=self.data)
                    self.check_na(data = self.data)
                    self.check_duplicates(data= self.data)
                    self.overall_stats(data=self.data)
                    self.correlation(data=self.data)
                    self.normal(data=self.data)
                    self.box(data = self.data)
                    self.count(data = self.data)
                    self.reg(data=self.data)
                    self.groupby(data = self.data)
           
           
                if ext[-1] == "xlsx":
                    self.data= pd.read_excel(upload)
                    self.show_dataset(data= self.data)
                    self.check_data(data=self.data)
                    self.no_of_col_row(data=self.data)
                    self.check_na(data = self.data)
                    self.check_duplicates(data= self.data)
                    self.overall_stats(data=self.data)
                    self.correlation(data=self.data)
                    self.normal(data=self.data)
                    self.box(data = self.data)
                    self.count(data = self.data)
                    self.reg(data=self.data)
                    self.groupby(data = self.data)
        except Exception as e:
            raise SystemException(e,sys)

# 1.show dataset     
    def show_dataset(self,data): 
        try:      
            if st.checkbox("Preview Dataset", key = "see_data"):
                if st.button("First 10 data"):
                    st.dataframe(data.head(10))
                if st.button("LAST 10 DATASET"):
                    st.dataframe(data.tail(10))
        except Exception as e:
            raise SystemException(e,sys)

            
# 2.check the datatype of the dataset 
    def check_data(self, data):
        try:
            if st.checkbox("LEARN ABOUT DATATYPES OF ALL THE COLUMNS", key = "check_data"):
                st.text("DATATYPES OF THE COLUMNS ARE AS FOLLOWING")
                st.write(data.dtypes)
        except Exception as e:
            raise SystemException(e,sys)

# 3.CHECK THE NO. OF COLUMNS AND NO. OF ROWS 
    def no_of_col_row(self, data):
        try:
            col_row = st.checkbox(" Check Number of Rows & Columns in your dataset?", key = "no of row col")
            if col_row:
                data_shape = st.radio("WHICH DIMENSION YOu WANT TO KNOW", ("ROWS", "COLUMNS"), key= "radio_button1")
            
                if data_shape == 'ROWS':
                    st.text("NUMBER OF ROWS")
                    st.text(data.shape[0])
                if data_shape == "COLUMNS":
                    st.text("NUMBER OF COLUMNS")
                    st.write(data.shape[1])
                    st.write("NAME OF EACH COLUMNS AS FOLLOWS", data.columns)
        except Exception as e:
            raise SystemException(e,sys)
# 4.CHECK THE MISSING VALUE OF THE IN THE DATAFRAME 
    def check_na(self , data):
        try:       
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
        except Exception as e:
            raise SystemException(e,sys)
# 5.FOR THE DUPLICATES VALUE IN YOUR COLUMNS 

    def check_duplicates(self, data):
        try:
            duplicate= st.checkbox("Do you want to check for duplicate values", key = "duplicate")
            if duplicate:
                test = data.duplicated().any()
                if test == True :
                    st.warning("This dataset contains the duplicate values")
                    dup  = st.selectbox("Do you want to Rmeove Duplicate Values", ("Select one", "SEE","Yes", "No"), key = "check_duplicate")
                    if dup == "Yes":
                        data = data.drop_duplicates(inplace= True)
                        st.text("Duplicates have been removed")
                    if dup == "No":
                        st.text ("ok No problem")
                    if dup == "SEE":
                        st.write(data[data.duplicated(keep = False)])
                else : 
                    st.text("there are no duplicate columns")
        except Exception as e:
            raise SystemException(e,sys)
#6.OVERALL STATISTICS OF THE USERS 
    def overall_stats(self, data):
        try:
            overall_stat = st.checkbox("SUMMARY STATISTICS OF THE DATASET", key = "summary")
            if overall_stat:
                st.write(data.describe(include= 'all'))
        except Exception as e:
            raise SystemException(e,sys)
            
# 7.GET CORRELATION STATISTICS BETWEEN THE COLUMNS 
    def correlation(self, data):
        try:
            check = st.selectbox("Do you want to see the correlations between Columns?",("Select one","YES", "NO"), key = "corr")
            if check == "YES":
                st.set_option('deprecation.showPyplotGlobalUse', False)
                sns.heatmap(data.corr(method = 'pearson',numeric_only=True), cmap = "YlGnBu", annot = True)
                st.pyplot()
                st.write(data.corr(method = 'pearson',numeric_only=True))
            if check == "NO":
                st.text("You selected not to check the correlation")
        except Exception as e:
            raise SystemException(e,sys)
# 8.GET TO CHECK IF THE DATA SET IS NORMALLY DISTRIBUTE OR NOT THROUGH DISPLOT
    def normal(self, data):
        try:
            value = st.selectbox("Would like to see the distribution of the dataset??", ("select one", "Yes", "No"), key = "normal")
            if value == "Yes":
                new = data.select_dtypes(exclude= "object")
                for i in new.columns:
                    st.set_option('deprecation.showPyplotGlobalUse', False)
                    sns.distplot(new[i])
                    st.pyplot()
        except Exception as e:
            raise SystemException(e,sys)           
# 9. GET TO SEE IF THE COUNT OF CATEGORICAL DATA SETS IN YOUR DATA SETS 
    def count(self, data):
        try:
            if st.checkbox("DO YOU WANT TO PLOT THE COUNT PLOTS???"):
                value =  st.selectbox("Would like to see the count_plot of the columns??", (list(data.columns)), key = "count")
                st.write(f"YOU WANT TO SEE THE COUNT_PLOT OF THE FOLLOWING COLUMN {value}") 
                st.set_option('deprecation.showPyplotGlobalUse', False)
                cx= sns.countplot(x = value, data= data)
                for bars in cx.containers:
                        cx.bar_label(bars)
                st.pyplot()
        except Exception as e:
            raise SystemException(e,sys)
        
# 10. Get Box PLot plot of your data 
    def box(self, data):
        try:
            if st.checkbox("DO YOU WANT TO PLOT BOX PLOT???", key = "BOX_PLOTING"):
                box_val =  st.selectbox("Would like to see the box_plot of the columns??", (list(data.columns)), key = "box_plot")
                st.write(f"YOU WANT TO SEE THE BOX_PLOT OF THE FOLLOWING COLUMN {box_val}")    
                st.set_option('deprecation.showPyplotGlobalUse', False)
                bx = sns.boxplot(x = box_val, data= data)
                for boxes in bx.containers:
                        bx.bar_label(boxes)
                st.pyplot()
        except Exception as e:
            st.write(e)
            
# Check for the reg-plot for regression between individual attrbutes of datasets
    def reg(self, data):
        try:
            if st.checkbox("DO YOU WANT REG PLOT???", key = "REG_PLOTING"):
                X_VAL =  st.selectbox("Would like to see the REG_PLOT of the columns-CHOOSE X COLUMN VALUE??", (list(data.columns)), key = "reg1_plot")
                Y_VAL =  st.selectbox("Would like to see the REG_PLOT of the columns-CHOOSE Y COLUMN VALUE??", (list(data.columns)), key = "reg2_plot")
                st.write(f"YOU WANT TO SEE THE REG_PLOT {X_VAL} vs {Y_VAL} ON THE FOLLOWING COLUMN ") 
                st.set_option('deprecation.showPyplotGlobalUse', False)
                cx= sns.jointplot(x = X_VAL, y = Y_VAL, data= data, kind = 'reg')
                regline= cx.ax_joint.get_lines()[0]
                regline.set_color("red")
                st.pyplot(cx)

                st.write(data.corr(method = 'pearson',numeric_only=True))
                    
        except Exception as e:
                raise SystemException(e,sys)


                
# 11. PERFORM GROUP BY    
    def groupby(self, data):
        try:    
            button1 = st.checkbox("Click Here if you want to perform the group by option")
            if button1:
                group_name = st.selectbox(("choose the column you want to group?"), 
                                        ((list(data.columns))))
                
                st.text(f'this is the coulumn you choose for the group by - {group_name}')
                
                agg_name = st.selectbox(("choose the column you want to aggregate?"), 
                                        ((list(data.columns))))
                
                st.text(f'this is the coulumn you choose for the aggregate by - {agg_name}')
                
                agg = st.selectbox("Choose the aggreagation you want to do on the dataframe", ("select one", "sum", "count", "mean","median","std","var","mad","prod", "max", "min"))
                
                if agg !="select one": 
                    sum_grouped =eval(f"data.groupby('{group_name}', as_index=False)['{agg_name}'].{agg}()")
                    st.dataframe(sum_grouped)
                
                    if st.checkbox("would you like to plot the data"):
                        st.set_option('deprecation.showPyplotGlobalUse', False)
                        ax1= sns.barplot(x = group_name,y= agg_name ,data = sum_grouped)
                        for bars in ax1.containers:
                            ax1.bar_label(bars)
                        st.pyplot()
        except Exception as e:
            raise SystemException(e,sys)
if __name__ == "__main__":
    data_profile_streamlit()
  
       
        
        







