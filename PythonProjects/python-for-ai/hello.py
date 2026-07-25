



person = {
    "name": "poorna",
    "age": 21,
    "city": "bengaluru"
}

person["age"]

person["lisence"]=True


person.keys()
person.values()
person.items()



empty=()

num={1,2,3,4,5}
fruits=set(["apple","bannana","apple"])
set(fruits)

scores=[22,34,55,33,22,32,34,56]
unique_scores=set(scores)



def greet():
    print("hello")

greet()
greet()


def check_weather():
    temprature=16
    if temprature>25:
        print("its hot")
    else:
        print("temp is normal")

check_weather()



def greet(name):
    print(f"hello {name} how r u ?")

greet("poorna")


def greet(f_name,l_name):
    print(f"hi {f_name}{l_name} how r u?")

greet("poorna","chandra")


