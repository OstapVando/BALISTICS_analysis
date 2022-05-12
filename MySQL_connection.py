#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pymysql
import pandas as pd

#connction settings
connection = pymysql.connect(
    host='localhost',
    port=int(3306),
    user='root',
    passwd='Cam12p',
    db='pp_db'
)

#reading database
df = pd.read_sql_query("SELECT * FROM balistic_data", connection)

print(df)


# In[6]:


df.head()


# In[ ]:




