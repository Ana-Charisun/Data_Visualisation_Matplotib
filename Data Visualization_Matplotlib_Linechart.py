#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


# LINE GRAPH MODE


# In[18]:


mpl.rcParams.update(mpl.rcParamsDefault)


# In[19]:


x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
y = (5, 17, 15, 23, 22, 30, 35, 40, 45, 50)
plt.plot(x,y)
plt.show()


# In[6]:


plt.figure(figsize=(10,5)) # ADDING SIZE
x = (2, 3, 4, 5, 6, 7, 8, 9, 10)
y = (17, 15, 23, 22, 30, 35, 80, 45, 55)
plt.plot(x,y)
plt.show()


# In[20]:


plt.style.use('seaborn-darkgrid') # ADDING DARK STYLING 


# In[9]:


plt.figure(figsize=(11,6)) # ADDING SIZE
x = (2, 3, 4, 5, 6, 7, 8, 9, 10)
y = (17, 15, 23, 22, 30, 35, 80, 45, 55)
plt.plot(x,y)
plt.show()


# In[10]:


plt.figure(figsize=(11,6)) 
x = (2, 3, 4, 5, 6, 7, 8, 9, 10)
y = (17, 15, 23, 22, 30, 35, 80, 45, 55)
plt.plot(x,y, 'r-') #ADDING COLOR
plt.xlabel("x - Satuan") #ADDING LABEL
plt.ylabel("y - Jumlah")
plt.show()


# In[13]:


plt.figure(figsize=(11,6)) 
x = (2, 3, 4, 5, 6, 7, 8, 9, 10)
y1 = (17, 15, 23, 22, 30, 35, 80, 45, 55)
y2 = (13, 15, 33, 22, 34, 45, 84, 65, 50)
y3 = (10, 11, 23, 32, 40, 25, 60, 35, 45)
plt.plot(x,y1, 'r-', label = "Garis 1") #ADDING LEGEND
plt.plot(x,y2, 'g-', label = "Garis 2")
plt.plot(x,y3, 'b-', label = "Garis 3")
plt.xlabel("x - Satuan") 
plt.ylabel("y - Jumlah")
plt.legend()
plt.tight_layout() #SETTING TIGHT
plt.show()


# In[48]:


plt.figure(figsize=(11,6)) 
x = (2, 3, 4, 5, 6, 7, 8, 9, 10)
y1 = (17, 15, 23, 22, 30, 35, 80, 45, 55)
y2 = (13, 15, 33, 22, 34, 45, 84, 65, 50)
y3 = (10, 11, 23, 32, 40, 25, 60, 35, 45)
plt.subplot(3,1,1)
plt.plot(x,y1, 'r-')

plt.subplot(3,1,2)
plt.plot(x,y2, 'g-')

plt.subplot(3,1,3)
plt.plot(x,y3, 'b-')

plt.tight_layout()
plt.show()


# In[24]:


plt.figure(figsize=(11,6)) 
x = (2, 3, 4, 5, 6, 7, 8, 9, 10)
y1 = (17, 15, 23, 22, 30, 35, 80, 45, 55)
y2 = (13, 15, 33, 22, 34, 45, 84, 65, 50)
y3 = (10, 11, 23, 32, 40, 25, 60, 35, 45)
plt.plot(x,y1, 'r-', label = "Garis 1", linestyle='--') #ADDING Line style
plt.plot(x,y2, 'g-', label = "Garis 2", linestyle='-.')
plt.plot(x,y3, 'b-', label = "Garis 3", linestyle=':')
plt.xlabel("x - Satuan") 
plt.ylabel("y - Jumlah")
plt.legend()
plt.show()


# In[29]:


plt.figure(figsize=(11,6)) 
x = (2, 3, 4, 5, 6, 7, 8, 9, 10)
y1 = (17, 15, 23, 22, 30, 35, 80, 45, 55)
y2 = (13, 15, 33, 22, 34, 45, 84, 65, 50)
y3 = (10, 11, 23, 32, 40, 25, 60, 35, 45)
plt.plot(x,y1, 'r-', label = "Garis 1", linewidth = 8) 
plt.plot(x,y2, 'g-', label = "Garis 2", linewidth = 8) #CHANGING LINE WIDTH
plt.plot(x,y3, 'b-', label = "Garis 3", linewidth = 8)
plt.xlabel("x - Satuan") 
plt.ylabel("y - Jumlah")
plt.legend()
plt.tight_layout()
plt.show()


# In[26]:


plt.figure(figsize=(11,6)) 
x = (2, 3, 4, 5, 6, 7, 8, 9, 10)
y1 = (17, 15, 23, 22, 30, 35, 80, 45, 55)
y2 = (13, 15, 33, 22, 34, 45, 84, 65, 50)
y3 = (10, 11, 23, 32, 40, 25, 60, 35, 45)
plt.plot(x,y1, 'r-', label = "Garis 1")
plt.plot(x,y2, 'g-', label = "Garis 2")
plt.plot(x,y3, 'b-', label = "Garis 3")
plt.fill_between(x,y1) #SHADING REGION
plt.fill_between(x,y2)
plt.fill_between(x,y3)
plt.xlabel("x - Satuan") 
plt.ylabel("y - Jumlah")
plt.legend()
plt.tight_layout()
plt.show()


# In[38]:


plt.figure(figsize=(11,6)) 
x = (2, 3, 4, 5, 6, 7, 8, 9, 10)
y1 = (17, 15, 23, 22, 30, 35, 80, 45, 55)
y2 = (13, 15, 33, 22, 34, 45, 84, 65, 50)
y3 = (10, 11, 23, 32, 40, 25, 60, 35, 45)
plt.plot(x,y1, 'r-', label = "Garis 1", linewidth = 2) 
plt.plot(x,y2, 'g-', label = "Garis 2", linewidth = 2)
plt.plot(x,y3, 'b-', label = "Garis 3", linewidth = 2)
plt.xlabel("x - Satuan") 
plt.ylabel("y - Jumlah")
plt.legend()
plt.grid(b=True , linestyle = '-.' , which = 'major' , color = 'y') # ADDING GRID
plt.tight_layout()
plt.show()


# In[49]:


plt.figure(figsize=(11,6)) 
ax = plt.axes()
ax.set_facecolor("yellow") # CHANGE BACKGROUND
x = (2, 3, 4, 5, 6, 7, 8, 9, 10)
y1 = (17, 15, 23, 22, 30, 35, 80, 45, 55)
y2 = (13, 15, 33, 22, 34, 45, 84, 65, 50)
y3 = (10, 11, 23, 32, 40, 25, 60, 35, 45)
plt.plot(x,y1, 'r-', label = "Garis 1", linewidth = 3) 
plt.plot(x,y2, 'g-', label = "Garis 2", linewidth = 3)
plt.plot(x,y3, 'b-', label = "Garis 3", linewidth = 3)
plt.xlabel("x - Satuan") 
plt.ylabel("y - Jumlah")
plt.legend()
plt.grid(b=True , linestyle = '-.' , which = 'major' , color = 'b') # ADDING GRID
plt.tight_layout()
plt.show()


# In[50]:


x = (2, 3, 4, 5, 6, 7, 8, 9, 10)
y1 = (17, 15, 23, 22, 30, 35, 80, 45, 55)
y2 = (13, 15, 33, 22, 34, 45, 84, 65, 50)
y3 = (10, 11, 23, 32, 40, 25, 60, 35, 45)

y4 = (10, 11, 33, 42, 20, 35, 50, 45, 55)
y5 = (18, 25, 23, 32, 14, 45, 44, 67, 20)
y6 = (19, 21, 29, 36, 50, 25, 10, 37, 40)

y7 = (15, 15, 33, 12, 34, 25, 60, 45, 50)
y8 = (10, 25, 36, 32, 24, 15, 44, 55, 56)
y9 = (16, 11, 25, 42, 47, 25, 40, 35, 47)

fig1 , ax1 = plt.subplots(nrows=3,ncols=3 , figsize = (20,20))
ax1[0,0].plot(x,y1,"tab:blue")
ax1[0,1].plot(x,y2,"tab:orange")
ax1[0,2].plot(x,y3,"tab:green")
ax1[1,0].plot(x,y4,"b-")
ax1[1,1].plot(x,y5,"r-")
ax1[1,2].plot(x,y6,"g-")
ax1[2,0].plot(x,y7,"m-")
ax1[2,1].plot(x,y8,"y-")
ax1[2,2].plot(x,y9,"k-")

plt.show()


# In[ ]:




