
# coding: utf-8

# In[54]:


class Triangle:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [i for i in range(self.n)]
    def findsides(self):
        self.sides = [float(input('Enter side '+str(i+1)+" : ")) for i in range(self.n)]        


# In[55]:


class Area(Triangle):
    def __init__(self):
        super(Area,self).__init__(3)
    def area(self):
        a,b,c = self.sides
        s = (a+b+c)/2
        ar = (s*(s-a)*(s-b)*(s-c))**0.5
        return "The area of te triangle is %f"%(ar)


# In[56]:


a1 = Area()
a1.findsides()
a1.area()

