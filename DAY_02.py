#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#                 DAY 2: STRING PRACTICE 


# In[ ]:


# How to print a value?


# In[2]:


print("30 days 30 hour challenge ")
print('30 days 30 hour challenge ')


# In[ ]:


# Assigning String To variable:


# In[4]:


HOURS="thirty"
print(HOURS)


# In[ ]:


# INDEX USING STRINGS


# In[5]:


Days = "Thirty Days"
print(Days[0])


# In[8]:


print(Days[7:])


# In[9]:


print(Days[4:8])


# In[10]:


print(Days[:-3])


# In[ ]:


# How to print the particular character from certain text?


# In[11]:


Challenge = "I will win"
print(Challenge [7:10])


# In[12]:


print(Challenge [4:])


# In[13]:


print(Challenge [::-5])


# In[14]:


print(Challenge [1:5])


# In[15]:


print(Challenge [4:5])


# In[16]:


Challenge = "I will win"
print(len(Challenge ))


# In[ ]:


# Convert string into lower character


# In[17]:


Challenge = "I will win"
print(Challenge.lower())


# In[ ]:


# String Concatenation: - Joining two strings


# In[19]:


a = "30 Days "
b = "30 Hours "
c=a+b
print(c)


# In[ ]:


# Adding Space during concatenation 


# In[20]:


a = "30 Days "
b = "30 Hours "
c=a + " " + b
print(c)


# In[ ]:


# Casefold() :  - Usage


# In[22]:


Text = "Thirty Days and thirty Hours"
x = Text.casefold()
print(x)


# In[23]:


Text = "Thirty Days and thirty Hours"
x = Text.capitalize()
print(x)


# In[24]:


Text = "Thirty Days and thirty Hours"
x = Text.find('and')
print(x)


# In[25]:


Text = "Thirty Days and thirty Hours"
x = Text.isalpha()
print(x)


# In[26]:


Text = "Thirty Days and thirty Hours"
x = Text.isalnum()
print(x)

