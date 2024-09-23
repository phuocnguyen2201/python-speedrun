# -*- coding: utf-8 -*-

numbers = []

for i in range(5):
    numbers.append(int(input("Give a number: ")))
    
print(f"Sum is: {sum(numbers)}")
print(f"Average is: {sum(numbers)/len(numbers):.3f}")
print("Numbers:", end=" ")
for i in numbers:
    print(i, end=" ")
print()


