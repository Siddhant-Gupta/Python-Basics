#!/usr/bin/env python
# coding: utf-8

# In[1]:


a='monika'


# In[2]:


print(a)


# In[3]:


type(a)


# In[4]:


a="monika"


# In[5]:


type(a)


# In[6]:


a='''monika'''


# In[7]:


type(a)


# In[8]:


b=2
print(b)
type(b)


# In[10]:


c=10+2j
print(c)
type(c)


# In[ ]:


#1.LIST#: Collection of homogenous and heterogenous items


# In[ ]:


# homogenous: same data types
#heterogenous: differnt data types


# In[11]:


#example of homogenous
p=[1, 2, 3, 4, 5]


# In[14]:


#example of heterogenous list
p=[1,2,3,4,3+4j,'monika', True]


# In[15]:


print(p)


# In[ ]:


#2.TUPLE: in round brackets- can have homogenous as well as heterogenous elements


# In[16]:


t=(1,2,3,4)# homogenous elements
tt=('monika','red',1.23,1+2j) #heterogenous elements


# In[ ]:


#different between list and tuple: tuples are immutable means you cannot deelte elements in tuple but in list , the elements can be mutable and elements can be chnaged.. whenever u want to add or deelte the leemnts, then list can be used. tuples are immutable types of data structure and lists are mutable sequence. tuple are in round brackets and list in square brackets


# In[18]:


#3. DICTIONARY: when we are storing key value pairs
#4. SETS: are enclosed by braces- stores heterogenous and homogebous elements
c={'name': 'monika', 'age':24, 'marks': 100}#dictionary
d={'monika',24,100.10}


# In[19]:


age=1


# In[20]:


age_=1


# In[21]:


age-=1


# In[22]:


age


# In[23]:


age-*=1


# In[24]:


age_*=1


# In[25]:


age


# In[26]:


#id command
a=23
id(a)


# In[27]:


b=23
id(b)


# In[ ]:


#d commands gives the unique id. it is the memory address. Python works on memory element. 
#Unique id is giving memory location of any number


# a=3
# b=0.4
# c=a/b
# print(c)

# In[28]:


a=3 
b=0.4 
c=a/b 
print(c)


# In[29]:


type(c)


# In[30]:


int(type(c))


# In[31]:


int(c)


# In[32]:


a=12
b=20
c=45
print(int(a),complex(b),str(c))


# In[33]:


#Basic input operation


# In[39]:


a=input("any number")
type(a)


# In[40]:


a=int(input("any number"))
type(a)


# In[41]:


a=input("first value")
b=input("second value")
c=a+b
print(c)


# In[42]:


a=int(input("first value"))
b=int(input("second value"))
c=a+b
print(c)


# In[45]:


#Arithmetic Operators
x=4
y=5
print(x*y)
print(x+y)
print(x-y)
print(x/y)
print(x//y)
print(x%y)
print(x**y)


# In[46]:


#Logical Operators
a=10
b=20
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)


# In[48]:


'hello'=='Hello'


# In[49]:


50=='50'


# In[52]:


25==25.2


# In[55]:


#BITWISE OPERATORS
#leftshift always doubles the number
9<<1 #BITWISE LEFTSHIFT once


# In[57]:


9<<2 #leftshift twice


# In[58]:


9<<3#leftshift thrice


# In[59]:


5<<4
#means 5x2=10,10x2=20,20x2=40,40x2=80


# In[60]:


2^2 #bitwise xor operator


# In[61]:


2^3


# In[62]:


10>>1 #right shift, halves the number


# In[63]:


10>>2 #right shift, halves the number 10 ka half is 5, 5 ka half is 2.5 
#and it gives a intger value and it will not work on float data type


# In[64]:


#assignment operators
a=10
b=20
print(a>b and a!=b)


# In[66]:


#identity operators
a=6
b=6
c=2
print(a is b)
print(b is c)
print(c is b)


# In[68]:


#membership operator
spam=['cat','bat','mat']
print(str('cat') in spam)
print(str('dog') in spam)


# In[70]:


#ordered property of list
example= ['string',23,23.34]
example2= [23,'string',23.34]
example==example2
#list follows a particular order, list is in proper order


# In[75]:


#indexing of list
l=[1,2,3,4,5,6,7,8,9,10]
print(l[0])
print(l[5:6])
print(l[3:5])#5th index will not be included
print(l[::])


# In[77]:


#list suports negative index
print(l[-1])
print(l[-9])


# In[ ]:




