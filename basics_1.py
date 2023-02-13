#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[7]:


#1 Check if a Given Key Already Exists in Dictionary
name = {1:"raj",2:"ravi",3:"jim",4:"rohan"} 
print(name[1]) 


# In[8]:


ol = int(input("provide a key (numeric): ")) 
print(ol in name)


# In[11]:


#2 Checks if the key is present, if not returns default value
name = {1:"raj",2:"ravi",3:"jim",4:"rohan"} 
ol = int(input("provide a key (numeric): ")) 
if(ol in name): 
    print("key is there") 
else: name[ol] ="day" 
print(name)


# In[13]:


#3 Write a Python program to check whether a given value already exists in a dictionary
name = {1:"raj",2:"ravi",3:"jim",4:"rohan"}
ol = input("provide a vlaue : ") 
if (ol in name.values()):
    print("the value is there")
else : 
    print("the value is not there") 


# In[14]:


#4 Create a Student nested dictionary
student = {1:{"a":"name1","b":"age1"},2:{"c":"name2","d":"age2"},3:{"e":"name3","f":"age3"}} 
student


# In[15]:


#5 Check whether the Student dictionary is Empty or not, print appropiate message
student = {1:{"a":"name1","b":"age1"},2:{"c":"name2","d":"age2"},3:{"e":"name3","f":"age3"}}
if len(student)>0:
    print("it is filled with data")
else:
    print("it is empty")


# In[16]:


#6 Sort a Student Dictionary by Key
name = {5:"raj",2:"ravi",3:"jim",4:"rohan"}
dict(sorted(name.items()))


# In[17]:


#7 Merge two given Student and Course dictionaries
name = {5:"raj",2:"ravi",9:"jim",8:"rohan"}
student = {1:{"a":"name1","b":"age1"},2:{"c":"name2","d":"age2"},3:{"e":"name3","f":"age3"}}
student.update(name)
student


# In[18]:


#8 Count the number of items in the Merged dictionary
print(len(student)) 


# In[20]:


#9 Remove any key from the Student dictionary
name = {1:"raj",2:"ravi",3:"jim",4:"rohan"} 
ol = int(input("give a key to delete: "))
dict.pop(name,ol)
print(name)


# In[ ]:


#10 Extract values of Particular Key from Nested Student Dictionary
name = {5:"raj",2:"ravi",9:"jim",8:"rohan"}
student = {1:{"a":"name1","b":"age1"},2:{"c":"name2","d":"age2"},3:{"e":"name3","f":"age3"}}
student.update(name)
ol =int(input("give a key: ")) 
print(student[ol])


# In[ ]:




