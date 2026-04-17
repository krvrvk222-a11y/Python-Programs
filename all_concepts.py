#Write a program to input 2 numbers & print their sum.

# a = int(input("Enter the first number :"))
# b = int(input("Enter the second number :"))
# sum = a + b
# print(sum)

#_________________________________________________________
#Write a program to input side of a square & print its area

# a = int(input("Enter the side of the square :"))
# area = a**2
# print("The area of the square is :",area)

#________________________________________________________________
#Write a program to input 2 floating numbers & print thier average 

# a = float(input("Enter the first number :"))
# b = float(input("Enter the second number :"))
# avg = (a+b)/2
# print("The average of the two numbers is :",avg)

# ___________________________________________________________________
#Write a program to input 2 int numbers a and b
#Print True if a is greater than or equal to b.If not print false

# a = int(input("Enter the first number :"))
# b = int(input("Enter the second number :"))
# if a > b or a == b :
#     print("True")
# else:
#     print("False")
#__________________________________________________________________
#Write a program to input user's  first name & print its length

# a = input("Enter your first name :")
# b = len(a)
# print("The length is :", b)

#__________________________________________________________________________
#Write a program to find the occurancy of '$' in a string

# text = "I have 3$ but i need 10$ can you give me 7$"
# a = text.count("$")
# print(a)

#___________________________________________________________________________
#Grade students based on marks 
# marks>= 90, grade = "A"
# 90 > marks >= 80,grade = "B"
# 80 > marks >= 70,grade = "C"
# 70> marks, Grade = "D"








# marks = int(input("Enter your marks :"))
# if marks >= 90:
#     print('Your grade is "A"')
# elif 90 > marks >= 80:
#     print('Your grade is "B"')
# elif 80 > marks >= 70:
#     print('Your grade is "C"')
# else:
#     print("Your grade is 'D'")

#________________________________________________________________________________________
#Write a program to check if a number entered by the user is odd or even.

# num = int(input("Enter the number :"))
# if num % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

#_____________________________________________________________________________________
#Write a program to find the greatest of 3 numbers by the user 

# a = int(input("Enter the first number :"))
# b = int(input("Enter the second number :"))
# c = int(input("Enter the third number :"))

# if a > b and a > c:
#     print(a,"A is the greater number")
# elif b > a and b > c:
#     print(b,"B is the greatest number")
# else:
#     print(c,"C is the greatest number")

#___________________________________________________________________________________________
#Write a program to check if a number is a multiple of 7 or not.

# num = int(input("Enter the number :"))
# if num % 7 == 0:
#     print("The number is multiple by 7")
# else:
#     print("The number is not multiple by 7")

#_______________________________________________________________________________________________________-
#Write a program to ask the user to enter names of their 3 movies & store them in a list

# movies = []
# mov1 = input("Enter the first moive :")
# mov2 = input("Enter the second movie :")
# mov3 = input("Enter the third moive :")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

#____________________________________________________________________________________________________________________
#Write a program to check if a list contains a plaindrome of elements.

# lis1 = list(input("Enter the values :"))
# a = lis1.copy()
# a.reverse()
# lis2 = list(input("Enter the values :"))
# b = lis2.copy()
# b.reverse()

# if lis1 == a and lis2 == b:
#     print("Both are plaindrome")
# elif lis1 == a and lis2 != b:
#     print("First list is plaindorme and second list is not palindrome")
# elif lis1 != a and lis2 == b:
#     print("The first list not plaindrome and second list is palindrome")
# else :
#     print("Both the list are not palindrome")

#_________________________________________________________________________________________________________________
#Write a program to count the number of students with the "A" grade in the following tuple

# tup = ("C","D","A","A","B","B","A")
# print(tup.count("A"))

#___________________________________________________________________________________________________________________________
#Write a program to store above values in a list & sort them from "A" to "D"

# lis = ["C","D","A","A","B","B","A"]
# lis.sort()
# print(lis)

#___________________________________________________________________________________________________


#Write a python code to find the first non-Repeating charcter in a stirng 

# def nonrepeat_ch(n):
#     char_count = {}
#     for ch in n:
#         char_count[ch] = char_count.get(ch , 0) + 1
#     for ch in n :
#         if char_count[ch] == 1:
#             return ch
# a = input("Enter the string :")
# result = nonrepeat_ch(a)

# if result :
#     print("The first non repeat charcter is :", result)
# else:
#     print("There are no repeating values") 

#______________________________________________________________________________________________________________________
#Store the following word meanings in a python dictionary:
#table: "a piece of furniture","list of facts & figures"

#cat : " a small animal"

# my_dict = {
#     "table" : ("a piece of furniture","list of facts & figures"),
#     "cat" : "a small animal"
# }
# print(my_dict)
# print(type(my_dict))
#___________________________________________________________________________________________________
#You are given a list of subjects for students. Assume one classroom is required for 1 subject.
#How many classrooms are needed by all the students

# sub = {"python","java","c++","javascript","java","python","java","c++","c"}
# tot = len(sub)
# print("The total number of classrooms required by the students are :",tot)
# print(sub)
#______________________________________________________________________________________________________________
#Write a program to enter marks of 3 subjects from the user and store them in a dictonary.
#Start with an empty dictionary & add one by one. Use subject name as key & makrs as value

# dic = {}
# a = int(input("Enter the maths marks :"))
# dic.update({"math" : a})

# b = int(input("Enter the chemistry marks :"))
# dic.update({"che" : b})

# c = int(input("Enter the phyics marks :"))
# dic.update({"phy" : c})

# print(dic)
# print(type(dic))
#_______________________________________________________________________________________________________________________
#Figure out a way  to store 9 & 9.0 as seprate values in the set 

# a = {9,"9.0"}
# print(a)

#___________________________________________________________________________________________________________________
                       #While loop:

#Print numbers from 1 to 100

# i = 1
# while i <= 100:
#     print(i)
#     i += 1
#____________________________________________________________________________________________________
#Print numbers from 100 to 1

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1
#_________________________________________________________________________________
#Print the multiplication table of a number n

# n = 1
# while n <= 10:
#     print(n * 2)
#     n += 1
#______________________________________________________________________________________________
#Print the elements of the following list using a loop

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx +=1
#____________________________________________________________________________________________
#Search for a number x in this tuple using loop

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("Enter a number to be searched :"))
# idx = 0
# while idx < len(nums):
#     if nums[idx] == x:
#         print("The number is found at index :", idx)
#     idx += 1
#_________________________________________________________________________________________________________

                      #FOR LOOP
#Print the elements of the following list using a loop

# nums = [1,4,9,16,25,36,49,81,100]

# for i in nums:
#     print(i)
#______________________________________________________________________________________________
#Search for a number x in this tuple using loop

# nums = [1,4,9,16,25,36,49,81,100]
# x = int(input("Enter the number to be searched :"))
# a = 0
# for i in nums:
#     if i == x:
#         print("The number found at index", a)
#     a += 1
#_________________________________________________________________________________________________
                   #for and range

#Print numbers from 1 to 100

# for i in range(1, 101,1):
#     print(i)
#___________________________________________________________________________________________________________
#Print numbers from 100 to 1

# for i in range(100,0,-1):
#     print(i)
#_________________________________________________________________________________
#Print the multiplication table of a number n

# n = int(input("Enter the number :"))
# for i in range(1,11,1):
#     print(i * n)
#__________________________________________________________________________________________

#Write a program to find the sum of first n numbers (using while)

# n = int(input("Enter the number :"))
# sum = 0
# for i in range (1,n+1):
#     sum = sum  + i
# print(sum)
#___________________________________________________________________________________________
#Write a program to find the factioral of first n numbers (using for)

# n = int(input("Enter the number :"))
# sum = 1
# for i in range(1,n+1):
#     sum = sum * i
# print("The factoral of",n,"is =",sum)
#_____________________________________________________________________________________________________

                            #FUNCTIONS

#Write a program to print the length of a list.

# movies = ["endgame","infinity war","jersey","civil war", "no way home"]
# cities = ["hyd","bnr","vizag","chennai","kerla","pune"]

# def count_len(list):
#     return len(list)

# print(count_len(movies))
# print(count_len(cities))
#______________________________________________________________________________

#Write a program to print the elements of list in single line.

# movies = ["endgame","infinity war","jersey","civil war", "no way home"]
# cities = ["hyd","bnr","vizag","chennai","kerla","pune"]

# def print_list(list):
#     for i in list:
#         print(i, end =" ")

# print_list(cities)
# print_list(movies)
#________________________________________________________________________________________

#Write a function to find the factorial of n

# def fact():
#     n = int(input("Enter the number :"))
#     a = 1
#     for i in range(1,n + 1,1):
#         a = a * i
#     print(a)

# fact()

#__________________________________________________________________________________________________
#Write a function to convert usd to INR

# def convt():
#     inr = 83
#     usd = int(input("Enter the dollars to convert :"))
#     n = inr * usd
#     print(usd,"usd is equal to =",n,"INR")

# convt()
#____________________________________________________________________________________________________

#Write a function to input a number is the number is odd-->string"ODD" , even--->string"even"

# def out():
#     n = int(input("Enter the number :"))
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "ODD"

# print(out())




# print("krv", end="$")  #end is used if we want to print next line in one line. If we provide any symbol like $ instead of space it will print krv$karthik
# print("karthik")
#______________________________________________________________________________________________________
                      #Recursion

#Write a recursive to print factorial of a number 

# def factorial(n):
#     if n == 0 or n == 1:      # base case
#         return 1
#     return n * factorial(n - 1)

# num = 5
# result = factorial(num)
# print("Factorial of", num, "is", result)

#__________________________________________________________________________________________
#Write a recursive function to calculate the sum of first n natrual numbers

# def sum_natural(n):
#     if n == 0:          # base case
#         return 0
#     return n + sum_natural(n - 1)
# num = 3
# print("Sum of first", num, "natural numbers is", sum_natural(num))

#_______________________________________________________________________________________________________
#Write a recursive function to print all elements in a list 


#_____________________________________________________________________________
                           #File I/O


#Modes in the file I/O

# "r": It is used to open text file for reading
# "w": Open for writing,truncating the file first
# "x": Create a new file and open it for writing
# "a": Open for writing,appending to the end of the file if it exists
# "b": Binary mode
# "t": text mode (default)
# "+": open a disk file for updating(reading and writing)
# "r+": Open for reading and writing. The pointer is position at the beginning of the file 
# "w+": open for reading and writing. The file is created if it doesn't exist.Otherwise it is truncated
# "a+": Read and append . The pointer is at the end


#_____________________________________________________________________________________________________
                         #OOPS

# ABSTRACTION: 
# Hiding the implemntation details of a class and only showing the essential features to the user.
    #(Basically hides useless info for the user and shows usefull details or output)

#ENCAPSULATION: 
# Wrapping data and functions into a single unit(Object)

#INHERITANCE: 
# WHEN ONE CLASSS CHILD DERIVES OR TAKES THE PROPERTIES 
# & METHODS OF THE PARENT CLASS OR BASE CLASS IS CALLED INHERITANCE

# There are 3 types:
#Single inheritance , multi-level inheritance, Multiple inheritance

# multi-level inheritance : In this one class inheites the properties from parent class 
# and from that class another class inherites the properties 

# Multiple inheritance: One class can inhertes two parent class properties
 
# Ex: 
# class Car:
#     @staticmethod
#     def start():
#         print("car started")
#     @staticmethod
#     def stop():
#         print("car stopped")
# class Maruthicar(Car):
#     def __init__(self,name):
#         self.name = name

# car1 = Maruthicar("Swift")
# print(car1.name)
# car1.start()


# POLYMORPHISM: Polymorphism means one thing having many forms — the same function name
#  can work differently depending on the object.
# 
#   (operator overloading)
#When the same operator is allowed to have diferent meaning according to the content

# Operators and Dunder functions 
#a+b   a.__add__(b)
#a-b  a.__sub__(b)
#a*b  a.__mul__(b)
#a/b  a.__truediv____(b)  4
#a%b  a.__mod____(b)  4









#  SUPER():This is used to access methods of the parent class
# Ex : # In this type is defined in the parent class so if we want to use in the child class we use super()

# class Car:
#     def __init__(self,type):
#         self.type = type
    
# class Toyatocar(Car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name = name 

# car1=Toyatocar("prius","disel")
# print(car1.type)


#    Methods
  # static methos : @staticmethod
  # class method : (cls)
  # instance method (self)

# @staticmethod: Methods that don't use the self parameter(work at class level)
# This don't need objects 

# @classmethod : A classmethod is a method that works on the class itself, not on objects.
# It uses cls instead of self.
# Ex: 
# class person:
#     name = "anonymous"
#     @classmethod
#     def changename(cls,name):
#         cls.name = name 
# p1 = person()
# p1.changename("krv")
# print(person.name)


# @property: If we want to change after assing the values we use this
#Ex: 
# class Student:
#     def __init__(self,phy,che,math):
#         self.phy = phy
#         self.che = che
#         self.math = math 
#     def percentage(self):  
#         print(str((self.phy+ self.che + self.math) / 3) + "%")
# stud1 = Student(99,97,99)
# stud1.percentage()

# If we want to change the marks in the future we can change but it will get changed in the particular subject not in the percentage

# class Student:
#     def __init__(self,phy,che,math):
#         self.phy = phy
#         self.che = che
#         self.math = math 
    
#     @property
#     def percentage(self):
#         return str((self.phy + self.che + self.math) /3) + "%"
# stu1 = Student(98,97,99)
# print(stu1.percentage)
# # If we want to change phy marks 
# stu1.phy = 86
# print(stu1.percentage)
        






#Del keyword : Used to delete object properties or objects itself

# del s1.name 
# del s1
# Ex:
# class Student:
#     def __init__(self,name):
#         self.name = name

# s1 = Student("Krv")
# print(s1.name)
# del s1
# print(s1)

#Private and public 
#Private : Private attributes & methods are meant to be used only within the class and are not accessible from outside the class
#  we can give private object or private attribut like     __classname (double underscore)

#_________________________________________________________________________________________________
# Create student class that takes name & marks of 3 subjects as arguments in constructor.
#Then create a method to print the average


# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def avg(self):
#         num = 0
#         for val in self.marks:
#             num += val
#         print("Hi",self.name,"Your average is :",num/3)

# s1 = student("krv",[97,95,99])
# print(s1.name,s1.marks)
# s1.avg()

# s2 = student("karthik",[96,94,99])
# print(s2.name,s2.marks)
# s2.avg()
#___________________________________________________________________

#Create account class with 2 attributes - balance & account no.
#Create method for debit,credit & printing the balance.

# class account():
#     def __init__(self,bal,acc):
#         self.balance = bal
#         self.account_no = acc

#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs.",amount,"was debited")
#         print("The total balance is :",self.balance())

#     def credit(self,amount):
#         self.balance += amount
#         print("Rs.",amount,"is credited")
#         print("The total balance is :",self.balance())


# acc1 = account(1000,1234)
# acc1.debit(300)
# acc1.credit(500)

#_________________________________________________________________________________________

# Create a class Student with:

# Attributes: name, marks

# Methods:

# update_marks(new_marks) → update the student's marks

# print_details() → print name and marks

# class Student():
#     def __init__(self,name,marks):
#         self.name = name 
#         self.marks = marks 
#     def updated_marks (self,new_marks):
#         self.marks = new_marks
#         print("Marks got updated :",self.marks)

# s1=Student("Krv",98)
# s1.updated_marks(90)
# print(s1.name,s1.marks)
#________________________________________________________________________________________
# Create a class Car with:

# Attributes: brand, speed

# Methods:

# accelerate(value) → increase speed

# brake(value) → decrease speed

# show_speed() → print current speed

# class Car:
#     def __init__(self,brand,speed):
#         self.brand = brand 
#         self.speed = speed
    
#     def accelerate(self,value):
#         self.speed += value
#         print("Speed got increased by :",value)
#         print("The current speed is :",self.speed)
    
#     def brake(self,value):
#         self.speed -= value
#         print("The speed is decreased by :",value)
#         print("The current speed is :",self.speed)
    
#     def show_speed(self):
#         print("The speed of",self.brand,"is",self.speed)

# car1= Car("BMW",120)
# print(car1.brand)
# print(car1.speed)
# car1.accelerate(30)
# car1.brake(40)
# car1.show_speed()
#_____________________________________________________________________________________________________

# Create a class Movie with:

# Attributes:

# name

# available_seats

# Methods:

# book_tickets(count) → reduce available seats

# cancel_tickets(count) → increase available seats

# show_status() → print movie name & seats left

# class Movie:
#     def __init__(self, name, available_seats):
#         self.name = name
#         self.available_seats = available_seats

#     def book_tickets(self, count):
#         if count <= 0:
#             print("Invalid ticket count")
#         elif count > self.available_seats:
#             print("Not enough seats available")
#         else:
#             self.available_seats -= count
#             print(f"{count} ticket(s) booked successfully")

#     def cancel_tickets(self, count):
#         if count <= 0:
#             print("Invalid ticket count")
#         else:
#             self.available_seats += count
#             print(f"{count} ticket(s) cancelled successfully")

#     def show_status(self):
#         print("Movie Name:", self.name)
#         print("Seats Available:", self.available_seats)


#_________________________________________________________________________________________________________

# Define a circle class to create a circle with radius r using constucutor 
#Define area() method of the class which calculates the area of the circle 
#Define a perimeter()method of the class which allows you too calculate the perimeter of the circle

# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
    
#     def area(self):
#         cal1 = 3.14 * self.radius**2
#         print("The area of the circle is :",cal1)

#     def perimeter(self):
#         cal2 = 2 * 3.14 * self.radius
#         print("The perimeter of the circle is :",cal2)

# c1 = Circle(8)
# c1.area()
# c1.perimeter()
#_____________________________________________________________________________________________________

#Define a employee class with attributes role,department & salary.
#This class also a showdetails() method.
  #Create an engineer class that inherits properties from employee & has additional atrributes:name & age 

# class Employee:
#     def __init__(self,role,dept,salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showdetails (self):
#         print("role =",self.role)
#         print("dept =",self.dept)
#         print("salary =",self.salary)
    
# class Engineer(Employee):
#     def __init__(self,name,age,role,dept,salary):
#         self.name = name 
#         self.age = age 
#         super().__init__(role,dept,salary)

#     def showdetails(self):
#         print("name =",self.name)
#         print("age =",self.age)
#         super().showdetails()

# e1 = Engineer("krv",23,"developer","IT",40000)
# e1.showdetails()
# #________________________________________________________________________________________________________________

# Create a parent class Vehicle with:

# brand

# model

# price

# Child class Car with:

# color

# year

# Tasks:

# Use super() to call parent constructor

# Override showdetails() and display all details      

# class Vehicle:
#     def __init__(self,brand,model,price):
#         self.brand = brand 
#         self.model = model
#         self.price = price

#     def showdetails(self):
#         print("brand =",self.brand)
#         print("Model =",self.model)
#         print("price =",self.price)
           
# class Car(Vehicle):
#     def __init__(self,color,year,brand,model,price):
#         self.color = color
#         self.year = year
#         super().__init__(brand,model,price)
    
#     def showdetails(self):
#         print("Color =",self.color)
#         print("year =",self.year)
#         super().showdetails()

# c1 = Car('White',2025,"Toyota","Fortuner",500000)
# c1.showdetails()
#_______________________________________________________________________________________________________



