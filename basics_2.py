#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[8]:


#1 Create a 5X2 integer array from a range between 0 to 100 such that the difference between each element is 5
print("Creating 5X2 array using np.arange")
sampleArray = np.arange(0, 100, 10)
sampleArray = sampleArray.reshape(5,2)
print (sampleArray)


# In[9]:


#2 Create a 8X3 integer array and split the array into four equal-sized sub-arrays
print("Creating 8X3 array using np.arange")
sampleArray = np.arange(10, 34, 1)
sampleArray = sampleArray.reshape(8,3)
print (sampleArray)

print("\nDividing 8X3 array into 4 sub array\n")
subArrays = np.split(sampleArray, 4) 
print(subArrays)


# In[10]:


#3 For a given 2D array, print max value from axis 0 and min value fom axis 1
print("Printing Original array")
sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]]) 
print (sampleArray)

minOfAxisOne = np.amin(sampleArray, 1) 
print("Printing amin Of Axis 1")
print(minOfAxisOne)

maxOfAxisOne = np.amax(sampleArray, 0) 
print("Printing amax Of Axis 0")
print(maxOfAxisOne)


# In[11]:


#4 For a given 3D array, delete the second column and insert the following new column its place
print("Printing Original array")
sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]]) 
print (sampleArray)

print("Array after deleting column 2 on axis 1")
sampleArray = np.delete(sampleArray , 1, axis = 1) 
print (sampleArray)

arr = np.array([[10,10,10]])

print("Array after inserting column 2 on axis 1")
sampleArray = np.insert(sampleArray , 1, arr, axis = 1) 
print (sampleArray)


# In[12]:


#5 Write a python program to display cube of all members from to a given number
l = [1, 2, 3, 4]
res = [pow(i, 3) for i in l] # Cube List using list comprehension
print(res)


# In[16]:


#6 Write a program to count number of items for a given dictionary with more than 1 key
def main():
    d = {'A' : [1, 2, 3, 4, 5, 6, 7, 8, 9],'B' : 34,'C' : 12,'D' : [7, 8, 9, 6, 4] }
    print(sum([len(d[x]) for x in d if isinstance(d[x], list)])) # using list comprehension
if __name__ == '__main__':
    main()


# In[18]:


#7 Write a program to get the maximum and minimum value of dicionary
my_dict = {'x':50, 'y':58, 'z': 56}
key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))
print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])


# In[19]:


#8 Write  a program to sum all the values of a dictionary
def returnSum(dict):
    return sum(dict.values())
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))


# In[20]:


#9 write  a program to generate random values using numpy array
np.random.rand(3,2)


# In[21]:


#10 write a program to calulate mean, median, standard deviation and variance using numpy arrary for a given array
array = np.arange(10)
print(array)
  
r1 = np.mean(array)
print("\nMean: ", r1)

r2 = np.median(array)
print("\nMedian: ", r2)

r3 = np.std(array)
print("\nstd: ", r3)
  
r4 = np.var(array)
print("\nvariance: ", r4)


# In[ ]:




