
# coding: utf-8

# In[10]:

import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import re
data = pd.read_csv('/Users/minnawin/PythonWorkInProgress/orders.tsv', sep="\t")
df = DataFrame(data)
print(df.head())


# In[8]:

items = df.item_name
print(items)


# In[11]:

print(df.item_price)


# In[28]:

most_ordered = df.item_name.value_counts()
print("Most ordered item:                    Number:\n")
print("=======================================================\n%s  ")%(most_ordered)


# In[30]:

ten_most_ordered = df.item_name.value_counts()[:9]
print(most_ordered)


# In[33]:

df.item_name.value_counts()[:10].plot(kind='bar')


# In[34]:

#Convert the item_price into float, after you remove the '$'
df['item_price'] = df['item_price'].str.replace('$','')
df['item_price'] = df['item_price'].astype(float)

print(df['item_price'])


# In[35]:

orders = df.groupby('order_id').sum()
orders.head()
orders['item_price'].describe()


# In[42]:

#Average number of items per order
#First, get the total number of items per order id
total_num_items = df.groupby('order_id')['quantity'].sum()
#print(total_num_items)
#Then calculate the average/mean
avg_num_items_per_order = total_num_items.mean()
print("Average number of items per order:  %.2f")%(avg_num_items_per_order)


# In[ ]:



