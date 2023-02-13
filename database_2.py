#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas


# In[39]:


import pandas as pd
import numpy as np


# In[47]:


#1 Load the given data set using pandas function and display first 5 records
dt=pd.read_csv('/home/student/61/dataset.csv')
dt
dt.head(5)
#2 Load the given data set using pandas function and display last 5 records
dt.tail(5)
#3 Display all the column names for the given data set
dt.columns
#4 Drop City and Hobbies columns from dataframe.
dt.drop(['Permanant City','Email.id'],axis=1)
#5 Replace the M/F column to Gender for the entire dataset.
dt.rename(columns={'M/F':'Gender'})
#6 Display all the Females who belong to Ahmedabod city
dt[(dt['Permanant City']=='Ahemdabad')&(dt['M/F']=='Female')]
#7 Display average score for PG percentage column.
dt['PG Avg till now'].mean()
#8  Create a new dataframe with columns: Student ID, Studet_ Name, Course and PG Score.
dt1=pd.DataFrame(dt,columns=['Student_ID','Student_Name','Course','PG Avg till now'])
dt1
#9 Displsy top 5 records of students having grade above 60% in UG and PG
dt[dt['Graduation_Tot']>60].head(2)
#10 Display total number of rows and columns for the given dataset
dt.shape
#11 Delete the rows of students who score below 60% in PG.
dt1=dt[dt['PG Avg till now']<=80]
dt1
dt1.drop(dt1.index)
#12 Display the total count of male and fomale students in each prognamme
dt['M/F'].value_counts()
#13 Replace all the null values (if any) with a default value for the City for the given dataset
dt['Permanant City']=dt['Permanant City'].replace(np.nan,'Ahemdabad')
#14 Display the average score of PG for all male and female students in each programme.
dt.groupby(['M/F'])['PG Avg till now'].mean()
#15 Give an example of navigating data frames using iloc method
dt.iloc[3:]
dt.iloc[:9]


# In[ ]:




