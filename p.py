name="poorna"
age=21
height=6.5
print(name)
print(type(age))
int_height=int(height)
print(int_height)


age=99
if age<= 5:
    print("ticket free")
elif age<=12:
    print("pay  as child")   
elif age<=18 or age<=60 :
    print("pay as adult")
else:
    print("pay full wages")

num=int(input("enter a num"))
if num % 2==0:
    print("even")
else:
    print("odd")

num= int(input("enter a num"))
for i in range(1,11): 
 print(f"{num} x {i}={num*i}")

def add (a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
a=int(input("enter a value"))
b=int(input("enter b value"))
print(add(a,b))
print(mul(a,b))
print(sub(a,b))   

fruits=["apple","bannana","cherry"]
print(fruits[-3])
 
numbers=[10,20,30,40]
total=0
for num in numbers:
    total=total+num
print(total)

numbers=[10,20,30,40]
double=[]   
for num in numbers:
    double.append(num*2)
print("doubled",double)

student_marks = {"poorna": 85, "chandra": 90, "tejaswi": 78}
for student in student_marks:
    print(student)

students = ["Anand", "Geetha", "Kumar"]
marks = [85, 90, 78]
student_marks={}
for i in range(len(students)):
    student_marks[students[i]]=marks[i]
print(student_marks)




