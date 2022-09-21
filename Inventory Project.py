#!/usr/bin/env python
# coding: utf-8

# In[34]:


#The initial invintory problem and we are sorting them into seperate list. 
#First I want to pull apart the strings and integers
inv = ['box of noodles', 25,
      'plastic cups', 45,
      'lucky charms cereal', 90,
      'bandaids', 30]
#Here I am sorting only string in the invintory list
for product in inv:
    if(type(product) == str):
        print(product)
        


# In[30]:


#Now I'm sorting only intigers
for count in inv:
    if(type(count)== int):
        print(count)


# In[52]:


#Now that we can DO that, lets try something else. Pull apart the strings and integers into empty lists 
#labled product and count

inv = ['box of noodles', 25,
      'plastic cups', 45,
      'lucky charms cereal', 90,
      'bandaids', 30]
product = []
count = []

#We have our empty bins above. now use 'isinstance' and elif to determine if the values are string or integer
#and sort them into the appropreate bin or list

for item in inv:
    #if Item is a string
    if isinstance(item,str):
        #append item to product list
        product.append(item)
    elif isinstance(item, int):
        count.append(item)
print(product,count)


# In[55]:


inv = ['box of noodles', 25,
      'plastic cups', 45,
      'lucky charms cereal', 90,
      'bandaids', 30]

#Setting up our empty buckets
product = []
count = []


# for each item in the list if it is a string place it in the product bucket
#if it is a integer place it in the count bucket
for item in inv:
    # if an item is a string
    if isinstance(item, str):
        # append the item to s list
        product.append(item)
    elif isinstance(item, int):
        count.append(item)
##pretty much were doing the same as above just making it look good with print statements.
#Notice how the orintation of the numbers do not change from the list. noodles still matches up with 25, cups still 
#match up with 45 and so on. 
    
##print(product, count)
print('*******************************************')
print('these are a list of the products:')
print(product)
print('********************************************')
print('these are a list of the count:')
print(count)


# In[47]:


print('these are a list of the products')
print(product)


# In[48]:


print('these are a list of the count')
print(count)

