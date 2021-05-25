#!/usr/bin/env python
# coding: utf-8

# ### 1. 라이브 선언하기

# In[43]:


# 데이터 조작 라이브러리 불러오기
import pandas as pd


# In[44]:


import psycopg2
import pandas as pd
from sqlalchemy import create_engine


# ### 2. 데이터 불러오기

# In[45]:


indata =     pd.read_csv("../dataset/kopo_decision_tree_all_new.csv")


# In[46]:


indata.shape


# In[47]:


indata.columns


# ### 3. 데이터 처리(컬럼 소문자로 변환)

# In[48]:


indata.columns = indata.columns.str.lower()


# In[49]:


indata.columns


# ### 4. 데이터 저장하기

# In[50]:


targerDbIp = "192.168.110.111"
targetDbPort = "5432"
targetDbId = "kopo"
targetDbPw = "kopo"
targetDbName = "kopodb"


# In[51]:


targetDbPrefix = "postgresql://"


# In[58]:


targetUrl = "{}{}:{}@{}:{}/{}".format(targetDbPrefix,
                                      targetDbId,
                                      targetDbPw,
                                      targerDbIp,
                                      targetDbPort,
                                      targetDbName)


# In[59]:


tableName = "pgout_kopo_sj"


# In[60]:


pg_kopo_engine = create_engine(targetUrl)


# In[64]:


try:
    indata.to_sql(name = tableName,
             con = pg_kopo_engine,
             if_exists = "replace", index = False)
    print("{} unload 성공!".format(tableName))
except Exception as e:
    print(e)


# In[57]:


targetUrl


# In[15]:





# In[ ]:





# In[ ]:




