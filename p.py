# name="poorna"
# age=21
# height=6.5
# print(name)
# print(type(age))
# int_height=int(height)
# print(int_height)


# age=99
# if age<= 5:
#     print("ticket free")
# elif age<=12:
#     print("pay  as child")   
# elif age<=18 or age<=60 :
#     print("pay as adult")
# else:
#     print("pay full wages")

# num=int(input("enter a num"))
# if num % 2==0:
#     print("even")
# else:
#     print("odd")

# num= int(input("enter a num"))
# for i in range(1,11): 
#  print(f"{num} x {i}={num*i}")

# def add (a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# a=int(input("enter a value"))
# b=int(input("enter b value"))
# print(add(a,b))
# print(mul(a,b))
# print(sub(a,b))   

# fruits=["apple","bannana","cherry"]
# print(fruits[-3])
 
# numbers=[10,20,30,40]
# total=0
# for num in numbers:
#     total=total+num
# print(total)

# numbers=[10,20,30,40]
# double=[]   
# for num in numbers:
#     double.append(num*2)
# print("doubled",double)

# student_marks = {"poorna": 85, "chandra": 90, "tejaswi": 78}
# for student in student_marks:
#     print(student)

# students = ["Anand", "Geetha", "Kumar"]
# marks = [85, 90, 78]
# student_marks={}
# for i in range(len(students)):    
#     student_marks[students[i]]=marks[i]
# print(student_marks)

# class car:
#     def __init__ (self, brand,model) :
#        self.brand=brand
#        self.model=model
#     def dis_info(self):
#          # print(f"car:{self.brand},model:{self.model}")
#        print(f"Car Brand: {self.brand}, Model: {self.model}") 
# my_car= car("mahindra","xuv700")
# my_car.dis_info()


# class dog:
#    def __init__(self,name,breed):
#         self.name=name
#         self.breed=breed
#    def bark(self):
#        print(f"Name:{self.name} , breed:{self.breed}")
# nayi1=dog("rocky","germanshepherd")
# nayi2=dog("chintu","pug")
# nayi1.bark()
# nayi2.bark()

# class human:
#     def __init__(self,name,age):
#           self.name=name
#           self.age=age
#     def walk (self):
#           print(f"Name:{self.name} of,age:{self.age} is walking")

# n1=human("poorna",22)
# n2=human("Alex",20)
# n1.walk()


# abstraction
# class car:
#     def startengine(self):
#         print("engine started")
#     def accelerate(self):
#         print("car started")
#     def brake(self):
#         print("The car stopped")
# c1=car()
# c1.accelerate()
# c1.startengine()

#  encapsulation

# class database:
#     def __init__(self):
#         self.storage={}                here --> if u replace it as __storage then it will be an private attribute where it cant be acessed by other methods
#     def write(self,key,value):
#         self.storage[key]=value
#     def read(self,key):
#         if key in self.storage:
#             print(self.storage[key])
#         else :
#             print("data doesnt exist")
# db=database()
# db.write("name","poorna")
# db.read("name")
# print(db.storage)

# Inheritance
# class user:
#     def __init__(self,username):
#         self.username=username
#     def login(self):
#         print(F"{self.username} logined sucessfully")
# class admin(user):
#     def delete_user(self):
#         print("user has been deleted")
# a=admin("porna")
# a.login()
# a.delete_user()

# polymorphism

# class animals:

#     # def make_sound(self):                       ----->here make_sound is an method that has many forms
#         print("animal is making sound")
# class dog(animals):
#     def make_sound(self):
#         print("bark")
# class cat(animals):
#     def make_sound(self):
#         print("meow")
# anima_l=[dog(),cat()]
# for animal in anima_l:
#     animal.make_sound()

# error and exception handling
# . SYNTAX ERROR ----> MISSING A COLON OR BRACES DURING THE EXECUTION OF THE PROGRAM
#. RUNTIME EXCEPTION --> ERROR OCCURED DURING THE EXECUTION OF THE PROGRAM
# a=int(input("a:"))
# b=int(input("b:"))
# try:
#     print(a/b)
# except Exception as e:
#                                 #  ----------> HERE Exception IS AN CLASS THAT INVOLVE ALL ERROR 
#     print(f"there is an error:{e}")
# else:
#     print("enu error illa")
# finally:
#     print("program ended, if error comes or not i dont care in your program but its executed")


# try:
#     boy= str(input("enter boy name u want to marry?"))
#     if boy!="poorna":
#         print("you shd marry only poorna")
#     else:
#         print("good u have got ur gem")
# except Exception as e:
#     print(f"error:{e}")
# finally:
#     print("make sure u have selected correct gem poorna")


# FILE HANDLING ----> used to read from or wite to a files
# and also used to store data permanently


# file = open ("notes.txt","r")
# content = file.read()
# print(content)
# file.close()
        
    
# Mode
# 'r' Read (default mode)
# 'w' Write (overwrites if file exists)
# 'a' Append (adds content at the end) Add data without deleting old
# 'x' Create (fails if file exists)
# 'b' Binary mode
# 't' Text mode (default)