#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip  install Pandas Scikit-learn Numpy h5py Cython Flask Seaborn Scipy Numpy Matplotlib Ipython Jupyter Sympy Nose')


# In[2]:


import seaborn

iris = seaborn.load_dataset("iris")
type(iris)


# In[3]:


pandas.core.frame.DateFrame


# import pandas
# pandas._version _
# 

# In[5]:


import pandas
pandas.__version__


# In[6]:


import seaborn

iris = seaborn.load_dataset("iris")
type(iris)


# In[7]:


iris.head()


# In[8]:


iris.count()


# In[9]:


iris['species'].unique()


# In[10]:


seaborn.pairplot(iris, hue="species")


# In[ ]:




