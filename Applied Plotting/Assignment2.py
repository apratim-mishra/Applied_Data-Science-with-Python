
# coding: utf-8

# # Assignment 2
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# An NOAA dataset has been stored in the file `data/C2A2_data/BinnedCsvs_d400/e8bf6d64ac2036488261e1f8e527e9213ceb2987a0f2ee8800dacd80.csv`. The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) [Daily Global Historical Climatology Network](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt) (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
# 
# Each row in the assignment datafile corresponds to a single observation.
# 
# The following variables are provided to you:
# 
# * **id** : station identification code
# * **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# * **element** : indicator of element type
#     * TMAX : Maximum temperature (tenths of degrees C)
#     * TMIN : Minimum temperature (tenths of degrees C)
# * **value** : data value for element (tenths of degrees C)
# 
# For this assignment, you must:
# 
# 1. Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
# 2. Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
# 3. Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
# 4. Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
# 
# The data you have been given is near **Newark, Delaware, United States**, and the stations the data comes from are shown on the map below.

# In[2]:

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(400,'e8bf6d64ac2036488261e1f8e527e9213ceb2987a0f2ee8800dacd80')


# In[ ]:




# In[3]:

df = pd.read_csv('data/C2A2_data/BinnedCsvs_d400/e8bf6d64ac2036488261e1f8e527e9213ceb2987a0f2ee8800dacd80.csv')


# In[ ]:




# In[4]:

df.shape


# In[ ]:




# In[5]:

df.sort(['ID','Date']).head()


# In[6]:

df.tail()


# In[ ]:




# In[7]:

df.dtypes


# In[8]:

df['Year'],df['Month-Date']=zip(*df['Date'].apply(lambda x:(x[:4],x[5:])))


# In[ ]:




# In[9]:

df = df[df['Month-Date'] != '02-29']


# In[10]:

df.head()


# In[11]:

import numpy as np
import pandas as pd


# In[12]:

df.dtypes


# In[ ]:




# In[ ]:




# In[ ]:




# In[13]:

min_1 = df[(df['Element'] == 'TMIN') & (df['Year'] != '2015')].groupby('Month-Date').aggregate({'Data_Value':np.min})


# In[14]:

min_1


# In[ ]:




# In[15]:


max_1 = df[(df['Element'] == 'TMAX') & (df['Year'] != '2015')].groupby('Month-Date').aggregate({'Data_Value':np.max})
min_2015 = df[(df['Element'] == 'TMIN') & (df['Year'] == '2015')].groupby('Month-Date').aggregate({'Data_Value':np.min})
max_2015 = df[(df['Element'] == 'TMAX') & (df['Year'] == '2015')].groupby('Month-Date').aggregate({'Data_Value':np.max})


# min_2015

# In[16]:

min_2015


# In[48]:

min_specified=np.where(min_2015['Data_Value']<min_1['Data_Value'])


# In[49]:

min_specified


# In[50]:

max_specified=np.where(max_2015['Data_Value']>max_1['Data_Value'])


# In[51]:

max_specified


# In[111]:

plt.figure(figsize=(20,10))
plt.grid(linewidth=2, alpha=0.4)
plt.plot(min_1.values, 'b', label='minimum')
plt.plot(max_1.values, 'g',label='maximum')
plt.scatter(min_specified, min_1.ix[min_specified],s=95 ,marker='^', c='r', label ='min_specified', alpha=0.9)
plt.scatter(max_specified, max_1.ix[max_specified] ,s=95, c='purple',marker='X', label='max_specified', alpha=0.9)
plt.gca().axis([-5, 370, -250, 650])
plt.xticks(range(0,len(min_1),30), min_1.index[range(0,len(min_1),30)] , alpha=0.7)
plt.xlabel('Day of the year', fontsize=20)
plt.ylabel('Temperature (Tens of Celsius)', fontsize=20)
plt.title('Temperature from 2005 to 2014 in Newark, Delaware', fontsize=20)
plt.legend(loc=2, frameon=False, mode='expand', fontsize=20)
plt.gca().fill_between(range(len(min_1)), min_1['Data_Value'], max_1['Data_Value'], facecolor='yellow', interpolate=True, alpha=0.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.show()


# In[ ]:



