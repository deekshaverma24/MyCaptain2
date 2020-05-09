#!/usr/bin/env python
# coding: utf-8

# ### Assigning elements to different lists

# In[2]:


MyList = [24,3.14,'C++']
print(MyList)

MyList.append(121)
print(MyList)


# ### Accessing elements from a tupule

# In[28]:



mytuple = ('b','a','r','m','i','t')

print(mytuple[0])  
print(mytuple[4])   


# ### Deleting different dictionary elements

# In[9]:



myDict = {1:'Ayush', 2:'Cabir', 3:'Dhruv', 4:'Erica', 5:'Farah', 6:'Geetu'}

del myDict[3]
print(myDict)

(myDict.pop(6)) 
print(myDict)
print(myDict.get(6))


# In[ ]:




