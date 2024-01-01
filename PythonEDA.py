#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# # Data Gathering
# 

# df=pd.read_csv(r"C:\Users\Rishav Banerjee\Documents\PythonProjectEDA\Diwali Sales Data.csv",encoding="unicode-escape")
# df

# In[7]:


df.shape


# In[8]:


df.head


# In[9]:


df.head()


# In[10]:


df.info()


# # Data Cleaning

# In[12]:


df.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[13]:


df.info()


# In[14]:


df.isnull().sum()


# In[15]:


df.dropna(inplace=True)


# In[16]:


df.info()


# In[17]:


df.isnull().sum()


# In[18]:


df['Amount']=df['Amount'].astype('int')


# In[19]:


df.info()


# In[21]:


df[['Amount','Orders','Age']].describe()


# # Exploratory Data Analysis

# # Gender

# In[27]:


a=sns.countplot(x='Gender',data=df)
for bars in a.containers:
    a.bar_label(bars)


# In[30]:


sales_gen_data=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sales_gen_data


# In[31]:


sns.barplot(x='Gender',y='Amount',data=sales_gen_data)


# #### From the above graphs we can conclude that the most of the buyers are female and the amount spend by females is more than males 

# # AGE

# In[34]:


a=sns.countplot(x="Age Group",data=df,hue='Gender')
for bars in a.containers:
    a.bar_label(bars)


# In[40]:


sales_age_data=df.groupby(['Age Group','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sales_age_data


# In[43]:


sns.barplot(x='Age Group',y='Amount',hue='Gender',data=sales_age_data)


# #### From the above graphs we can see that most of the buyers belong to the age group 26-35 and are females
# 

# # State

# In[47]:


orders_state_data=df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False)
orders_state_data


# In[56]:


sns.set(rc={'figure.figsize':(25,5)})
sns.barplot(x='State',y='Orders',data=orders_state_data)


# In[62]:


sales_state_data=df.groupby(['State','Gender'],as_index=False)['Amount'].sum().sort_values(by="Amount",ascending=False)
sales_state_data


# In[63]:


sns.barplot(x="State",y="Amount",hue="Gender",data=sales_state_data)


# #### From the above graphs we can observe that most of the top spending customers are females residing mainly in Uttar Pradesh,Maharashtra,Karnataka and Delhi

# # Marital Status

# In[72]:


sns.set(rc={'figure.figsize':(15,5)})
a=sns.countplot(x='Marital_Status',data=df,hue="Gender")
for bars in a.containers:
    a.bar_label(bars)


# In[70]:


sales_marital_data=df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sales_marital_data


# In[73]:


sns.barplot(x='Marital_Status',y='Amount',hue='Gender',data=sales_marital_data)


# #### From the above graphs we can observe that the top spenders are unmarried females
# 

# # Occupation

# In[96]:


sales_occ_data=df.groupby(["Occupation","Gender","Marital_Status"],as_index=False)['Amount'].sum().sort_values(by="Amount",ascending=False)
sales_occ_data


# In[97]:


sns.barplot(x="Occupation",y="Amount",hue='Gender',data=sales_occ_data)


# #### From the above graphs we can observe that most of the top customers are unmarried females working in Healthcare,IT sector and Aviation Industry

# # Conclusion

# #### Based on the data and the above graphs it can be concluded that most of top customers are unmarried females working in Healthcare,IT Sector and Aviation industry residing mainly in Uttar Pradesh,Maharashtra,Karnataka and Delhi

# In[ ]:




