
# coding: utf-8

# In[16]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')


# In[17]:

pwd


# In[18]:

data=pd.read_csv("dataset_2.csv")


# In[19]:

data.head()


# In[20]:

data.columns


# In[21]:

data.dtypes


# In[22]:

plt.style.use("seaborn")


# In[25]:

data.head()


# In[45]:

data=pd.read_csv("dataset_2.csv", index_col="Date")


# In[28]:

data.head


# In[29]:

data.shape


# In[30]:

data.index


# In[33]:

gdp1=pd.read_csv("gdp11.csv", index_col="Date")


# In[34]:

gdp1.head()


# In[36]:

gdp1.columns=["GDP_Value"]


# In[37]:

gdp1.head


# In[38]:

gdp1['GDP_Value']


# In[39]:

data.columns


# In[40]:

gdp1.dtypes


# In[43]:

data=data[['Personal consumption expenditures (PCE)','Goods']]


# In[44]:

data.head


# In[46]:

data.head()


# In[47]:

data.columns


# In[48]:

data=data[['Personal consumption expenditures (PCE)','Goods','Services']]


# In[50]:

data.head(5)


# In[51]:

gdp1.head(5)


# In[52]:

data.dtypes


# In[53]:

gdp1.dtypes


# In[54]:

data.index=pd.to_datetime(data.index)


# In[55]:

data.index


# In[56]:

gdp1.index=pd.to_datetime(gdp1.index)


# In[57]:

gdp1.index


# In[58]:

import datetime as dt
data.index= data.index.date_column.dt.to_period('M')


# In[60]:

data.index = data.index.map(lambda x: x.strftime('%B-%Y')) 


# In[61]:

data.index


# In[62]:

data.head(5)


# In[63]:

gdp1.index=gdp1.index.map(lambda x:x.strftime('%B-%Y'))


# In[64]:

gdp1.index


# In[66]:

gdp1.head(5)


# In[68]:

gdp1.shape


# In[69]:

data.shape


# In[70]:

data.index


# In[71]:

gdp1.index


# In[73]:

final=data.join(gdp1)


# In[74]:

final.head(5)


# In[75]:

final.dropna


# In[76]:

final.shape


# In[77]:

final.head(10)


# In[78]:

final=final.dropna()


# In[79]:

final.head(5)


# In[80]:

final.shape


# In[81]:

pd.tools.plotting.scatter_matrix(final)


# In[82]:

g = sns.pairplot(final, diag_kind='kde', size=2);


# In[83]:

plt.subplots_adjust(top=0.9)
g.fig.suptitle('Corelationship between GDP and other Economic Stats')


# In[84]:

corr = final.corr()


# In[85]:

sns.heatmap(corr)


# In[ ]:



