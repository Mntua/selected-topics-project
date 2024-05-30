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
# In[8]:


#FIELD ANALYSIS ...


# In[9]:


# 1. product type


# In[10]:


# Display product type distribution in the dataset.
pie_labels = df_input['Product type'].value_counts().index.to_list()
plt.pie(df_input['Product type'].value_counts(), autopct="%.2f%%", labels = pie_labels);
plt.title ("Product Type distribution");


# In[11]:


# 2. price


# In[12]:


# Price field value statistics
df_input['Price'].describe()


# In[13]:


# Draw the box plot for Price distribution
sns.boxplot(data=df_input, x="Price").set_title('Price Distribution');


# In[14]:


# Which product is having highest price ?
max_price = df_input["Price"].max()
df_input[df_input["Price"] == max_price]


# In[15]:


# Which product having lowest price?
min_price = df_input['Price'].min()
df_input[df_input['Price'] == min_price]


# In[16]:


# 3. availability


# In[17]:


print (df_input['Availability'].describe());
sns.boxplot(data=df_input, x="Availability").set_title("Availability Distribution");


# In[18]:


# Highest available products
df_input.sort_values("Availability", ascending=False).head(5)


# In[19]:


# Lowest available products
df_input.sort_values("Availability", ascending=True).head(5)


# In[20]:


# 4. number of products sold


# In[21]:


print (df_input['Number of products sold'].describe());
sns.boxplot(data=df_input, x="Number of products sold").set_title("Number of products sold - distribution");


# In[22]:


# 5. revenue generated


# In[23]:


print (df_input['Revenue generated'].describe());
sns.boxplot(data=df_input, x="Revenue generated").set_title("Revenue generated - distribution");


# In[24]:


# Observations having highest number of 'revenue generated'
df_input.sort_values('Revenue generated', ascending=False).head(3);


# In[25]:


# Observations having lowest nuber of 'Revenue generated'
df_input.sort_values('Revenue generated').head(3)


# In[26]:


# 6. customer demographics


# In[27]:


# Draw a plot for Customer demograohics
gender_labels = df_input['Customer demographics'].value_counts().index.to_list()
plt.pie(df_input['Customer demographics'].value_counts(), labels=gender_labels, autopct="%.2f%%");
plt.title("Customer demographics - distribution");


# In[28]:


# 7. stock levels


# In[29]:


print (df_input['Stock levels'].describe());

# Draw the box plot distribution
sns.boxplot(data=df_input, x="Stock levels").set_title("Stock levels - distribution");
