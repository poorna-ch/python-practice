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

class animals:

    # def make_sound(self):                       ----->here make_sound is an method that has many forms
        print("animal is making sound")
class dog(animals):
    def make_sound(self):
        print("bark")
class cat(animals):
    def make_sound(self):
        print("meow")
anima_l=[dog(),cat()]
for animal in anima_l:
    animal.make_sound()
        
    
