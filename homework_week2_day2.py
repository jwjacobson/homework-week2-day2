#!/usr/bin/python

# Exercise 1
# Create a list of numbers that are less than ten using l_1 and list comprehension

l_1 = [1,11,14,5,8,9]

new_list = [num for num in l_1 if num < 10]
print(new_list)

# Exercise 2
# Using list comprehension, create a list of names of 4 letters or more and capitalize each name
names1 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']

new_names1 = [name.title() for name in names1 if len(name) >=4]
print(new_names1)

names2 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']

new_names2 = [name.title() for name in names2 if isinstance(name, str) and len(name) >=4]
print(new_names2)
