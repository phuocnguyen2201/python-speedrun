# -*- coding: utf-8 -*-

name = input("Give your name: ")
height = float(input("Give height in meters: "))
weight = float(input("Give weight in kgs: "))

print(f"Your name is {name}, and you are {height}m tall, and your weight is {weight} kg.")
bmi = round(float(weight/(height ** 2)),2)
print(f"Your bmi is {bmi}")