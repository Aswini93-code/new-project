#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[13]:


data=pd.read_csv(r"Desktop\1. Weather Data.csv") #r for remove  the unicode error.


# In[14]:


data #view my data


# In[15]:


data.index #index start from 0 and end with 8784 ,also show default value 1


# In[17]:


data['Weather'].unique() #it will show  only the unique value,it can be applied to single column only,not a entire column


# In[20]:


data.nunique() #this will show the unique value count for each and ervery column


# In[21]:


data.count() # it shows the total no.of non null in each column.


# In[22]:


data['Weather'].value_counts() #in a column,it shows all the unique values with therir count.it can be applied on single column only


# In[23]:


data.info() #provides basic information about dataframes


# In[24]:


data.head(2)


# In[ ]:


#1.Find all the unique 'wind speed' values in the data.


# In[25]:


data.nunique()


# In[26]:


data['Wind Speed_km/h'].nunique()


# In[28]:


data['Wind Speed_km/h'].unique() 


# In[ ]:


#2.Find the numer of times when the weaher is exaclty clear.


# In[29]:


data.head(2)


# In[30]:


data.Weather.value_counts() #it will show about the counts of each element in weather column


# In[33]:


data[data.Weather=='Clear'] #fillering method


# In[35]:


data.groupby('Weather').get_group('Clear') #groupby method ,getgroup choose clear from weather column


# In[ ]:


#3.find he number of times wen wind speed was exaclty kkm/hr.


# In[37]:


data[data['Wind Speed_km/h']==4]


# In[ ]:


#3.find out all th null values in the data.


# In[39]:


data.isnull().sum() #this command will show about missing value count,here no missing value.


# In[40]:


data.notnull().sum() #it will show the present value count.


# In[ ]:


#rename the column name:


# In[42]:


data.rename(columns={'Weather':'Weather condition'}) #column name changed temporary


# In[43]:


data


# In[56]:


data.rename(columns={'Weather':'Weather condition'},inplace=True) #column name changed temporary permanently


# In[57]:


data.head()


# In[46]:


data.head(2)


# In[47]:


data.Visibility_km.mean() #find mean for visibilty, mean is the sum of data divided by the number of data-points


# In[48]:


data.Press_kPa.std() # find std for press-kpa,Standard deviation is a number that describes how spread out the values are.


# In[49]:


data['Rel Hum_%'].var() #is used to calculate variance of a given set of numbers.


# In[ ]:


#find all nstances when snow was recorded.


# In[50]:


data['Weather condition'].value_counts()


# In[52]:


data[data['Weather condition'] =='Snow'] #filltering method


# In[53]:


data[data['Weather condition'].str.contains('Snow')].head(50) #this will show related to snow in weather column,first 50 rows


# In[ ]:


#find all instance when speed is above24 and visibility is 25


# In[54]:


data[(data['Wind Speed_km/h']>24)&(data['Visibility_km']==25)]


# In[55]:


data.groupby('Weather condition').mean()


# In[ ]:


#show all the records where weather condition is fog


# In[58]:


data[data['Weather condition']=='Fog']


# In[59]:


#find all instances when weather is clear or visibility is above 40.


# In[60]:


data[(data['Weather condition']=='Clear')|(data['Visibility_km']>40)]


# In[61]:


#weather is clear and relative humidity is greater then 50 
# or
#visibilty is above 40


# In[62]:


data[(data['Weather condition']=='Clear')&(data['Rel Hum_%']>50)|(data['Visibility_km']>40)]


# In[ ]:




