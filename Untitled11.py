
# coding: utf-8

# In[11]:


def filter_long_words(words,n):
    counter = list()
    for i in words:
        if(len(i) > n):
            counter.append(i)
    return counter
l1= input("Enter the list of words : ")
new_list = l1.split(',')
x = int(input("Enter the threshold value : "))
print(filter_long_words(new_list,x))

