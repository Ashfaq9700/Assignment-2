# 1 Write a python script to add comments and print “Learning Python” on screen.
"""Solution print('"Learning Python"')"""

# 2 Write a python script to add multi line comments and print values of four variables, each in a new line. Variable contains any values.
"""" Solution Multi Line Comments"""
"""name = "shaik Ashfaq"
gender = "male"
age = 28
profession =  "Developer"

print(name,gender,age,profession,sep='\n')"""

# 3 Write a python script to print types of variables. Create 5 variables each of them containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)
"""Solution 
name , age , maritual_Status , hight , complexity = "MySirG" , 35 , True , 5.46 , 3+4j

print("Hello My Name is {0} and i am".format(name),type(name))

print("My Age is {age}".format(age = age),"and i am {ageType}".format(ageType=type(age)))

print("My Marital Status is {}".format(maritual_Status),"and i am {}".format(type(maritual_Status)))

print("My Hight is %3.2f"%(hight),"and i am ",type(hight))

print("My complexity is {0} and i am".format(complexity),type(complexity))"""

# 4 Write a python script to print the id of two variables containing the same integer values.
"""Solution
one = two = 10
print("Variable one and two are pointing to same Memory address ",id(one),id(two))
print(one is two)"""

# 5 Create four variables in a Python script and assign values of different data types to them. Write a Python script to print value, its type and id of each variable
"""Solution
name , age , martialStatus , hight = "Shaik Ashfaq" , 28 , True , 5.8
print(name,type(name),id(name))
print(age,type(age),id(age))
print(martialStatus,type(martialStatus),id(martialStatus))
print(hight,type(hight),id(hight))"""

# 6 Write a python script to print all the keywords
"""Solution
print(help("keywords"))"""

# 7 On Python shell use help() function and display the list of keywords
"""Solution
help("keywords")"""

# 8 Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some
#value to it. Write a python script to import A1 module in A0 and print value of the
#variable created in A0.py
"""Solution
import A2
from A2 import greet
#print(A2.greet)
print(greet) """

# 9 Name the keywords, used as data in the Python script.
"""Solution
True
False
None
"""

# 10 Write a python script to display the current date and time. First create variables to store date and time, then display date and time in proper format (like: 13-8-2022 and9:00 PM)
"""Solution 
import datetime

date_Time = datetime.datetime.now()
date_Time = date_Time.strftime("%d-%m-%Y %H:%M:%S")
print(date_Time)"""