



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


def cal_area(width,height):
    area=width*height
    return area
room_area=cal_area(10,12)
print(f"room size is {room_area}")


def sim_fn():
    num=[1,2,3,4,5]
    first_no=num[0]
    last_no=num[-1]
    return first_no,last_no
first_no,last_no=sim_fn()




import math
math.sqrt(20)

from math import sqrt ,pi

sqrt(90)

import random

random.randint(1,20)


import datetime

today=datetime.date.today
print(today)

addddddddddddddddddddddddddddddddddddddddddddddd

import os
import pandas as pd
import requests
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Paris weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=12.971599&longitude=77.594566&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)
#ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss


# Extract the daily data
daily_data = data['daily']

# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])

print(df)


# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('banglore weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

if not os.path.exists('data'):
    os.makedirs('data')
    
plt.savefig('data/weather_chart.png')
df.to_csv('data/banglore_weather.csv', index=False)

# Save the plot
plt.savefig('weather_chart.png')
plt.show()




class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed  

class cat:
    def __init__(self,name,color):
        self.name=name
        self.color=color

jerry=Dog(name="jerry",breed="labourdor")
jerry.name




class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"

# Create different configurations
# Using positional for required arg, named for optional
dev_config = APIConfig("sk-dev-key", max_tokens=50)

# Using all named arguments (clearest)
prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_tokens=1000)

# Access the configuration
print(dev_config.model)        # gpt-3.5-turbo
print(prod_config.model)       # gpt-4
print(prod_config.max_tokens)  # 1000





class DataValidator:
    def __init__(self):
        self.errors = []
    
    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid email: {email}")
            return False
        return True
    
    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}")
            return False
        return True
    
    def get_errors(self):
        return self.errors

# Use the validator
validator = DataValidator()

# Notice: we don't pass self, just the email
validator.validate_email(email="bad-email")
validator.validate_age(age=200)

# Or using positional arguments
validator.validate_email("another-bad-email")
validator.validate_age(150)

print(validator.get_errors())
# ['Invalid email: bad-email', 'Invalid age: 200', 'Invalid email: another-bad-email']





class Dog:
    def __init__(self,name):
       self.name=name
    def bark(self):
        print("bark")
jerry=Dog(name="jerry")
jerry.name
jerry.bark()



class animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        return f"{self.name} is eating"
    def sleep(self):
        return f"{self.name} is sleeping"
class Dog(animal):
    def bark(self):
        return f"{self.name} is barking"


dog1=Dog("tommy")
dog1.eat()


