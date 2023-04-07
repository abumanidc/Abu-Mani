#!/usr/bin/env python
# coding: utf-8
# In[1]:
#importing pandas as pd
import pandas as pd
# In[4]:
#loading csv file to the dataframe
df=pd.read_csv(r"C:\Users\aboom\Downloads\youtube_dataset.csv",encoding='ANSI')
# In[33]:
#To get an idea about the dataframe
df.head()
# In[10]:
#to get the name of the column names
df.columns
# In[16]:
#To check the size of the datdframe
df.size
# In[19]:
#to check the shape of the dataframe
df.shape
# In[15]:
# to check the datatype of columns
df.dtypes
# In[26]:
#to verify that dataframe is in the order of top 4000 subscribers
df.subscribers.is_monotonic_decreasing
# In[70]:
# Creating function to make code modular
def answer1():
    df_first1000 = df.head(1000)
    ans1 = df_first1000['channeltype'].value_counts(normalize=False)
    result = pd.DataFrame({
        'Channel Type': ans1.index,
        'Count': ans1.values
    })
    return result
# In[73]:
# calling function
df_answer_one=answer1()
print(df_answer_one)
# In[98]:
# to find the total number of types in channeltype column
df_answer_one.Count.sum()
# In[97]:
#to verify total number of null fields in the channeltype column
df3=df.head(1000)
df3['channeltype'].isnull().sum()
# In[ ]:
# In[88]:
#since the total count of distinct values is less than 1000, checking for null values
df_answer_one.isnull().sum()
# In[83]:
#loading to csv file in desktop
First1000 = df.head(1000)
First1000.to_csv(r"C:\Users\aboom\OneDrive\Desktop\FIRST1000.CSV", index = False, header=True)
# In[84]:
#to know the shape 
First1000.head()
# In[87]:
#Importing engine
from sqlalchemy import create_engine
# In[99]:
#importing pymysql
import pymysql
# In[106]:
#connecting to sql
engine=create_engine('mysql+pymysql://****:*****@127.0.0.1/abudatabase')
# In[107]:
#loading the top thousand channel database to sql
First1000.to_sql('top_thousand_channels',engine,index=False)
# In[108]:
#connection argument
conn=engine.connect()
# In[109]:
# to display the contents of the loaded csv
df_from_sql=pd.read_sql("SELECT* FROM abudatabase.top_thousand_channels",conn)
# In[110]:
# to know the shape of the loaded csv in sql
df_from_sql.head()
# In[ ]:
