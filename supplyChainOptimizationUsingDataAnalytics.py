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

# In[30]:


# 8. lead times


# In[31]:


print (df_input['Lead times'].describe());
sns.boxplot(data=df_input, x='Lead times').set_title('Lead times - distribution');


# In[32]:


# 9. order quantities


# In[33]:


print (df_input['Order quantities'].describe());
sns.boxplot(data=df_input, x='Order quantities').set_title("Order quantities - distribution");


# In[34]:


# 10. shipping times


# In[35]:


print(df_input['Shipping times'].describe());
sns.boxplot(data=df_input, x="Shipping times").set_title("Shipping times -distribution");


# In[36]:


# 11. shipping carriers


# In[37]:


# Draw pie chart
carrier_labels = df_input['Shipping carriers'].value_counts().index.to_list()
plt.pie(df_input['Shipping carriers'].value_counts(), labels=carrier_labels, autopct="%.2f%%");
plt.title('Shipping carriers - distribution');


# In[38]:


# 12. shipping costs


# In[39]:


print (df_input['Shipping costs'].describe())
sns.boxplot(data=df_input, x="Shipping costs").set_title ("Shipping costs - distribution");


# In[40]:


# 13. supplier name


# In[41]:


supplier_labels = df_input['Supplier name'].value_counts().index.to_list();
plt.pie(df_input['Supplier name'].value_counts(), labels=supplier_labels, autopct="%.2f%%");
plt.title('Supplier name - distribution');


# In[42]:


# 14. location


# In[43]:


location_labels = df_input['Location'].value_counts().index.to_list()
plt.pie(df_input['Location'].value_counts(), labels=location_labels, autopct="%.2f%%");
plt.title ("Location - distribution");


# In[44]:


# 15 lead time


# In[45]:


print (df_input['Lead time'].describe());
# Draw box plot
df_input['Lead time'].describe()
sns.boxplot(data=df_input, x="Lead time").set_title('Lead time - distribution');


# In[46]:


# 16. production volumes


# In[47]:


print (df_input['Production volumes'].describe());

# Draw boxplot
sns.boxplot(data=df_input, x="Production volumes").set_title("Production volumes distribution");


# In[48]:


# 17. manufacturing lead time


# In[49]:


print (df_input['Manufacturing lead time'].describe());

# Draw the boxplot
sns.boxplot(data=df_input, x="Manufacturing lead time").set_title("Manufacturing lead time  - distribution");


# In[50]:


# 18. manufacturing costs


# In[51]:


print (df_input['Manufacturing costs'].describe());

# Draw box plot
sns.boxplot(data=df_input, x="Manufacturing costs").set_title("Manufacturing costs - distribution");


# In[52]:


# 19. inspection results


# In[53]:


inspection_results_labels=df_input['Inspection results'].value_counts().index.to_list()

# Draw Pie chart
plt.pie(df_input['Inspection results'].value_counts(), labels=inspection_results_labels, autopct="%.2f%%");
plt.title("Inspection results - distribution");


# In[54]:


# 20. defect rates


# In[55]:


print(df_input['Defect rates'].describe());

# Draw box plot
sns.boxplot(data=df_input, x="Defect rates").set_title("Defect rates - distribution");


# In[56]:


# 21. transportation modes


# In[57]:


transportation_modes_labels=df_input['Transportation modes'].value_counts().index.to_list();

plt.pie(df_input['Transportation modes'].value_counts(), labels=transportation_modes_labels, autopct="%1.1f%%");
plt.title("Transportation modes - distribution");


# In[58]:


# 22. routes


# In[59]:


route_labels = df_input['Routes'].value_counts().index.to_list()

#Draw pie
plt.pie(df_input['Routes'].value_counts(), labels=route_labels, autopct="%1.1f%%");
plt.title("Routes - distribution");


# In[60]:


# 23. costs


# In[61]:


print(df_input['Costs'].describe());

# Draw the boxplot
sns.boxplot(data=df_input, x="Costs").set_title("Costs - distribution");


# In[62]:


# 24. price


# In[63]:


print(df_input['Price'].describe());

# Draw boxplot
sns.boxplot(data=df_input, x="Price").set_title("Price - distribution");


# In[64]:


#DEMAND FORECASTING


# In[65]:


# 1. products having high demand


# In[66]:


# Observations having high number of 'sold products'
df_input[["Product type","SKU","Number of products sold","Location"]].sort_values("Number of products sold", ascending=False).head(5)


# In[67]:


# 2. products having low demand


# In[68]:


# Observations having lowest number of 'sold products'
df_input[["Product type","SKU","Number of products sold"]].sort_values("Number of products sold").head(5)


# In[69]:


#LOCATION RANKING BASED ON 'PRODUCT SELLING'


# In[70]:


# Extract required fields to seperate data frame
df_loc_product_sell = df_input[["Location", "Number of products sold"]].copy()

#Group by location and include sum for each location groups
df_loc_product_sell=df_loc_product_sell.groupby('Location').sum()

# Rename the sum field
df_loc_product_sell.rename(columns={'Number of products sold':"SoldProducts"}, inplace=True)

# Sort the rows based on the sum of Sold products
df_loc_product_sell.sort_values(by="SoldProducts",ascending=False, inplace=True)


# In[71]:


# Draw the bar graph
plt.bar(df_loc_product_sell.index, df_loc_product_sell['SoldProducts']);
plt.title("Location vs Total products sold");


# In[72]:


#AVERAGE SALES OF EACH PRODUCT TYPE PER LOCATION


# In[73]:


# Create seperate data frame with product type, number of products sold and location
df_product_type_location = df_input[["Product type","Location", "Number of products sold"]].copy()

# Find the mean value of 'Number of Products sold'
df_product_type_location = df_product_type_location.groupby(["Location","Product type"]).mean()

# Rename the mean value column
df_product_type_location.rename({"Number of products sold":"Products sold - average"},axis = 1, inplace=True)

# Reset the index
df_product_type_location.reset_index(inplace=True)

#Draw the bar graph
sns.barplot(data=df_product_type_location,
            x="Location",
            y="Products sold - average",
            hue="Product type");


# In[74]:


#PRODUCT TYPES HAVING MORE DEFECT RATES


# In[75]:


df_product_type_defect= df_input[['Product type','Defect rates']].copy()

#Group by product types
df_product_type_defect = df_product_type_defect.groupby('Product type').mean()

# Rename the Defect rates column
df_product_type_defect.rename(columns={'Defect rates':'Average defect rates'}, inplace=True)

# Sort the Average defect rates column
df_product_type_defect.sort_values(by="Average defect rates", ascending=False, inplace=True)


# In[76]:


# Plot the line graph
plt.plot(df_product_type_defect);
plt.title("Average defect rates per the product types");


# In[77]:


#TRANSPORATION COST


# In[78]:


# Create a seperate data frame for Transportation cost analysis
df_transport_cost = df_input[["Product type", "Transportation modes", "Costs"]].copy()

# Segregate records based on the Transportation modes and find mean of each group
df_transport_cost = df_transport_cost.groupby('Transportation modes').mean('Costs')

# rename the mean field
df_transport_cost.rename(columns={"Costs":"Avg Costs"}, inplace=True)

#Sort the records based on the mean cost value
df_transport_cost.sort_values(by="Avg Costs",ascending=False, inplace=True)


# In[79]:


# Visualize the average values of each transportation
plt.plot(df_transport_cost);
plt.title ("Average costs of transportation modes");


# In[80]:


#LEAD TIMES OF EACH PRODUCT TYPE PER SUPPLIER


# In[81]:


# Create new data frame
df_supplier_product_type = df_input[['Product type', 'Supplier name', 'Lead time']].copy()

# Group the columns based on the supplier name , product type and find the mean of 'lead time' of each sub group.
df_supplier_product_type = df_supplier_product_type.groupby(['Supplier name', 'Product type']).mean('Lead time')

# Rename the mean column of Lead time
df_supplier_product_type.rename(columns={'Lead time':'Avg Lead time'}, inplace=True)

#Reset the index
df_supplier_product_type.reset_index(inplace=True);

#Draw the bar graph
sns.barplot(data=df_supplier_product_type,
            x="Supplier name",
            y="Avg Lead time",
            hue="Product type"). set_title("Average Lead time of suppliers");
