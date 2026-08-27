import streamlit as st
import pandas as pd


data = {
" Name " : [ " Arjun " , " Rahul " , " Priya " , " Anjali " ] ,
" Marks " : [85 , 72 , 91 , 68] ,
" Course " : [" Data Science " ," Python " ," AI " ," Data Science "]
}

df = pd . DataFrame ( data )

st . title ( " Student Data " )
st . dataframe ( df )
st . table ( df )

file=st . file_uploader("Please upload your file for further analysis","csv")
df = pd . read_csv ( r'C:\Users\Arjun Singh\Desktop\Streamlit\customer.csv' )
st.dataframe(df)

st . write ( " Number of rows : " , df . shape [0])
st . write ( " Number of columns : " , df . shape [1])


st . write ( " Columns : " )
st . write ( df . columns . tolist () )

st . write ( " Total Info ",df.info() )

st . write ( " Summary Statistics " )
st . dataframe ( df . describe () )

st . write ( " Missing Values " )
st . dataframe ( df . isnull () . sum () )


total_Income = df [ "Income" ]. sum ()
average_Income = df [ "Income" ]. mean ()
total_customer = len ( df )


st . write ( " Total Income of customer : " , total_Income)
st . write ( " Avg Income of customer : " , average_Income)
st . write ( " Number of Customer : " , total_customer)


average_Age = df [ "Customer_Age" ]. mean ()
st . write ( " Avg Age of customer : " , average_Age)


average_csc = df [ "Cust_Satisfaction_Score" ]. mean ()
st . write ( " Avg customer Satisfaction Score : " , average_csc)

# st . line_chart ( df["Income"] )

# st . bar_chart ( df["Income"] )

Education_Level = st . selectbox (" Select Category " ,df [ "Education_Level" ]. unique ())


filtered_df = df [
df [ "Education_Level" ] == Education_Level
]
st . dataframe ( filtered_df )