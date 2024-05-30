# In[1]:


# import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from IPython.display import Image


# In[3]:


# Read the data file
df_input = pd.read_csv("C:/Users/user/Desktop/selected/supply_chain_data.csv")


# In[4]:


# sample data frame input
df_input.head()


# In[5]:


# Shape of the data file
df_input.shape


# In[6]:


# Data file fields
df_input.info()


# In[7]:


# Is there any null value fields ?
df_input.isnull().sum().any()
