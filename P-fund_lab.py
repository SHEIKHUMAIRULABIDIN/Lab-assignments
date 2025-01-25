# # Lab7
# # Bug Fixing
# # Code 1
# def sub(x, y):
#     return x + y
# print(sub(3, 5))

# # Code 2
# def describe_pet(pet_name, animal_type='dog'):
#     print("\nI have a " , animal_type ,".")
#     print("My " , animal_type + "'s name is " , pet_name + ".")
# describe_pet('Koji', 'cat')

# # Code 3
# def type_of_int(i):
#     if i // 2 == 0:
#         return 'even'
#     else:
#         return 'odd'
# print(type_of_int(3))

# # Output 
# # Code 1
# def test(a):
#     def add(b):
#         a =+ 1
#         return a+b
#     return add
# func = test(4)
# print(func(4))

# # Code 2
# def return_none():
#    return
# print(return_none())

# C.write programms 
# def favorite_book(title):
#     print("One of my favorite books is " + title)
# favorite_book('Alice in Wonderland')
# # Code 2
# def max():
#     a = 10
#     b = 20
#     if a > b:
#         return a
#     else:
#         return b
# # Code 3
# def GCD(x, y):
#     while(y):
#         x, y = y, x % y
#     return x
# print(GCD(18, 24))
# # Code 4
# def describe_city(city, country="USA"):
#     print((city)," is in", (country))
# describe_city("New York")  
# describe_city("Los Angeles")  
# describe_city("Tokyo", "Japan")  

# LAB 8
# Correct the code
# Code 1
# def max_list( list ):
#     max = list[ 0 ]
#     for a in list:
#         if a > max:
#             max = a
#     return max
# print(max_list([1, 2, -8, 0]))
# # Code 2
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# del motorcycles[0]
# print(motorcycles)
# # COde 3
# def dupe_v1(x):
#   y = []
#   for i in x:
#     if i not in y:
#       y.append(i)
#   return y

# a = [1,2,3,4,3,2,1]
# print (a)
# print (dupe_v1(a))
# # B.Output
# # Code 1
# list1= [1,2,4,5,6,7,8]
# print("Negative Slicing:",list1[-4:-1])
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print("Odd number:", x[::2])
# # Code 2
# def multiply_list(elements):
#     t = 1
#     for x in elements:
#         t*= x
#     return t
# print(multiply_list([1,2,9]))
# # Code 3
# def add(x,lst=[] ):
#     if x not in lst:
#         lst.append(x)
#         return lst

# def main():
#     list1 = add(2)
#     print(list1)
#     list2 = add(3, [11, 12, 13, 14])
#     print(list2)
# main()
# # write program
# def invitation(lst):
#       for guest in lst:
#         print(guest,"you are invited")
# Guests=["Nofal", "Umer", "Ahmed", "Afridi"]
# invitation(Guests)
# del(Guests[0])
# Guests.insert(0,"Pofal")
# print ("New List:\n")
# invitation(Guests)
# # Code 3
# # Original list
# lst = [30, 1, 2, 1, 0]

# lst1 = lst.copy()
# lst1.append(40)
# print( lst1)

# lst2 = lst.copy()
# lst2.remove(1)  
# print( lst2)

# lst3 = lst.copy()
# lst3.pop(1) 
# print( lst3)

# lst4 = lst.copy()
# lst4.pop()  
# print( lst4)

# lst5 = lst.copy()
# lst5.sort()
# print( lst5)

# lst6 = lst.copy()
# lst6.reverse()
# print( lst6)
# # COde 4
# def printsquare():

#   square_list = []
#   for i in range(1, 8):  
#     square_list.append(i * i) 
#   return square_list

# squares = printsquare()
# print("List of squares:", squares)
# def countX(lst, x): 
#     return lst.count(x)
# a=countX([8, 6, 8, 10, 8, 20, 10, 8, 8], 8)
# print(a)
# strs = ['aa', 'BB', 'zz', 'CC']
# print (sorted(strs)) 
# print (sorted(strs, reverse=True))   

# test_list = [1, 4, 5, 8, 10] 
# print ("Original list : " , test_list) 
  
# # check sorted list  
# def linear_search(lst, element):
#     for i in range(len(lst)):
#        if lst[i] == element:
#            return i
#     return "not found"

# my_list = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
# element_to_find = 110

# result = linear_search(my_list, element_to_find)
# print(f"The position of {element_to_find} in the list is: {result}")


# def have_common_member(list1, list2):

#   set1 = set(list1)
#   set2 = set(list2)
#   return bool(set1.intersection(set2))

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# print(f"List1: {list1}, List2: {list2}, Have common members: {have_common_member(list1, list2)}") 

# list3 = [10, 20, 30]
# list4 = [40, 50, 60]
# print(f"List3: {list3}, List4: {list4}, Have common members: {have_common_member(list3, list4)}")
# import random

# def merge_sorted_lists(list1, list2):
#   """
#   Merges two sorted lists into a single sorted list.

#   Args:
#     list1: The first sorted list.
#     list2: The second sorted list.

#   Returns:
#     A new list containing the merged and sorted elements of both input lists.
#   """
#   merged_list =[]
#   i = 0
#   j = 0

#   while i < len(list1) and j < len(list2):
#     if list1[i] <= list2[j]:
#       merged_list.append(list1[i])
#       i += 1
#     else:
#       merged_list.append(list2[j])
#       j += 1

#   while i < len(list1):
#     merged_list.append(list1[i])
#     i += 1

#   while j < len(list2):
#     merged_list.append(list2[j])
#     j += 1

#   return merged_list


# list1 = sorted([random.randint(1, 50) for _ in range(5)])
# list2 = sorted([random.randint(1, 50) for _ in range(5)])

# print("List 1:", list1)
# print("List 2:", list2)

# merged_list = merge_sorted_lists(list1, list2)
# print("Merged Sorted List:", merged_list)

# t = (1, 2, 3)
# print(t)
# user_0={'username':'efermi','first':'enrico','last':'fermi',}
# for key, value in user_0.items():
#     print("\nKey: " ,key)
#     print("Value: " ,value)
# tuple1 = ("green", "red", "blue")
# tuple2 = tuple([7, 1, 2, 23, 4, 5])
# tuple3 = tuple1 + tuple2 
# print(tuple3)
# tuple3 = 2 * tuple1 
# print(tuple3)
# print(tuple2[2 : 4]) 
# print(tuple1[-1])
# def main():
#     d = {"red":4, "blue":1, "green":14, "yellow":2}
#     print(d["red"])
#     print(list(d.keys()))
#     print(list(d.values()))
#     print("blue" in d)
#     print("purple" in d)
#     d["blue"] += 10
#     print(d["blue"])
# main() 

  
  
# print("Our Buffet Menu:")
# original_menu = ("Pizza", "Pasta", "Salad", "Fries", "Ice Cream")
# for food in original_menu:
#     print("- ",(food))

# print("Our Buffet Menu:")
# updated_menu = ("Burgers", "Sushi", "Salad", "Fries", "Cake")
# print("\nUpdated Menu:")
# for food in updated_menu:
#     print("- ",(food))
# import random

# capitals = {
#     "Alabama": "Montgomery",
#     "Alaska": "Juneau",
#     "Arizona": "Phoenix",
#     "Arkansas": "Little Rock",
# }

# correct_count = 0
# incorrect_count = 0

# states = list(capitals.keys())
# random.shuffle(states)

# for state in states:
#     capital = capitals[state]
#     guess = input(f"What is the capital of {state}? ")
#     guess = guess.lower() 

#     if guess == capital.lower():
#         print("Correct!")
#         correct_count += 1
#     else:
#         print(f"Incorrect. The capital of {state} is {capital}.")
#         incorrect_count += 1

# print("\nGame Over!")
# print("Correct answers:", correct_count)
# print("Incorrect answers:", incorrect_count)

# favorite_places = {
#     "Umair": ["Paris", "Moscow", "Tokyo"],
#     "Umer": ["New York", "London", "Sydney"],
#     "Pofal": ["Karachi", "Islamabad", "Lahore"]
# }

# for person, places in favorite_places.items():
#     print((person),"likes the following places:")
#     for place in places:
#         print("- ",(place))
# import sys as s
# print(s.executable)
# print(s.getwindowsversion())
# import datetime 
# from datetime import date
# import time
# print(time.time())
# print(datetime.datetime.now())
# import math

# print(math.sqrt(25))  # Output: 5.0
# print(math.pi)        # Output: 3.141592653589793
# print(math.degrees(2)) # Output: 114.59155902616465
# import calendar  
# yy = 2017
# mm = 11
# print(calendar.month(yy, mm)) import sys
# import sys
# print(sys.argv)
# for i in range(len(sys.argv)):
#    if i==0:
#        print("The function is",sys.argv[0])
#    else:
#        print("Argument:",sys.argv[i])
# import numpy as np
# arr = np.array( [[ 1, 2, 3],[ 4, 2, 5]] ) 

# print("No. of dimensions: ", arr.ndim) 
# print("Shape of array: ", arr.shape) 
# print("Size of array: ", arr.size)
# import numpy as np

# zeros_array = np.zeros(10)
# ones_array = np.ones(10)
# fives_array = np.full(10, 5)  

# combined_array = np.concatenate((zeros_array, ones_array, fives_array))
# print(combined_array)
# import numpy as np

# data = np.arange(2, 11) 
# matrix = data.reshape(3, 3)

 # print(matrix)
# a = "STRING"
# i = 0
# while i < len(a):
#     c = a[i]
#     print(c)
#     i += 1 
# def my_function(x):
#    return x[::-1]

# mytxt = my_function("I wonder how this text looks like backwards")
# print(mytxt)
# s= "Welcome"
# for i in range(0, len(s), 2):
#     print(s[i], end = '')
# s = input("Enter a string: ")
# if "Python" in s:
#     print("Python", "is in", s)
# else:
#     print("Python", "is not in", s)
# str='cold'
# list_enumerate=list(enumerate(str))
# print("list enumerate:", list_enumerate)
# print("list length:", len(str))
# s1 = "Welcome to Python"
# s2 = s1.replace("o","abc")
# print(s2)
# a = "Python" + "String"
# b = "<" + a*3 + ">"
# print(b)
# name = "\t Umair \n" 

# print("Original Name:", name) 
# print("lstrip():", name.lstrip()) 
# print("rstrip():", name.rstrip()) 
# print("strip():", name.strip())
# color = input("What is your favorite color? ")

# top = color * 10
# bottom = color * 10 
# middle = color + " " * 8*len(color) + color

# print(top)
# print(middle)
# print(bottom)

# file=open('python.txt','r')
# print("using read() mode character wise:")
# s1=file.read(19)
# print(s1)
# f1=open("jj","w")
# f1.write("something")
# def main():
#     outfile=open("E:\\Umair's Projects\\python.txt","w")
#     outfile.write("Bill Clinton\n")
#     outfile.write("George Bush\n")
#     outfile.write("Barack Obama") 
#     print(outfile)
#     outfile.close()  
#     infile = open("E:\\Umair's Projects\\python.txt", "r")
#     contents = infile.read() 
#     infile.close()
#     print(contents)
# main()
# def main():
#     outfile=open("e:\\Umair's Projects\\python.txt","x")
#     outfile.write("var, account_balance, client_name")
#     outfile.write("var = 1\n account_balance = 1000.0\nclient_name = 'John Doe'") 
#     print(outfile)
#     outfile.close() 
#     infile = open("e:\\Umair's Projects\\python.txt", "r")
#     contents = infile.read() 
#     infile.close()
#     print(contents) 
# main()
# def file_read(filename):


#   try:
#     with open(filename, 'r') as file:
#       contents = file.read()
#     return contents
#   except FileNotFoundError:
#     print(f"Error: File '{filename}' not found.")
#     return None

# file_name = "python.txt"  
# file_content = file_read(file_name)

# if file_content:
#   print(file_content)
# original_sent = "The quick brown dog jumps over the lazy dog."
# old_word = "dog"
# new_word = "cat"

# words = original_sent.split()
# new_sent = []

# for word in words:
#     if word == old_word:
#         new_sent.append(new_word)
#     else:
#         new_sent.append(word)

# replaced_sent = " ".join(new_sent)
# print(replaced_sent)  
# name = input("Please enter your name: ")
# try:
#     with open("python.txt", "a") as file:
#         file.write("\n"+name + "\n")
#     print("Your name has been added to the guest list.")
# except FileNotFoundError:
#     print("Error: Unable to write to the file.")
# class A():
#     def __init__(self, i):
#         self.i = i
#     def display(self): 
#         print(self.i)

# a = A(10) 
# a.display()
# class Dog():
#     attr1 = "mammal"  
#     def fun(self): 
#         print("I'm a", self.attr1)

# Rodger = Dog()
# Rodger.fun() 
# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# class Person:  
#     # init method or constructor   
#     def __init__(self, name):  
#         self.name = name  
    
#     def say_hi(self):  
#         print('Hello, my name is', self.name)  
    
# p = Person('XXX')  
# p.say_hi()  
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#     def describe_restaurant(self):
#         print(f"Restaurant Name: {self.restaurant_name}")
#         print(f"Cuisine Type: {self.cuisine_type}")
#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is now open!")

# my_restaurant = Restaurant("Pizza Palace", "Italian")
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()
import os
database_path = os.path.abspath("your_database.db")
print(database_path)



















