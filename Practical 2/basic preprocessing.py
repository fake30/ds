import pandas as pd 
import numpy as np

iris = pd.read_csv("iris.csv")

# print(iris["variety"]=="Setosa")

# grouping
groups = iris.groupby("variety")
a = groups.get_group("Setosa")
print(a)


# filtering
data = pd.read_csv("Student_Marks.csv")

a= data.loc[(data["Marks"]<20) & (data["number_courses"]==3)]
print(a)

b= data.loc[data["Marks"]<20]
print(b)


# sorting
l1 = [4,5,9,6,3,1,7,8,5,1,3,9,4]
a1=sorted(l1, reverse=True)
print(a1)

t1 = ((4,5),(7,9),(5,4))
c = sorted(t1, reverse=False)
print(c)