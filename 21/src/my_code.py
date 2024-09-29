# -*- coding: utf-8 -*-
import random

def ask_number():
    numbers = []
    N = int(input("How many numbers? "))
    if N < 1:
        print("Error!")
        return
    for i in range(N):
        random_decimal = random.randint(100, 10000) / 100
        numbers.append(random_decimal)
    print("Following numbers were drawn, and written to file numbers.txt:")
    for number in numbers:
        print("{:.2f}".format(number), end=" ")

    return numbers

def sort_results(numbers):

    with open("numbers.txt", "w") as f:
        for number in numbers:
            f.write("{:.2f}\n".format(number))

    with open("numbers.txt") as f:
        numbers = [float(row.strip()) for row in f]
    numbers.sort()

    print("\nFollowing numbers were read, and sorted, from file numbers.txt:")
    for number in numbers:
        print("{:.2f}".format(number), end=" ")
    return numbers

def write_results(numbers, N):
    with open("results.txt", "w") as f:
        f.write("Num: {}\n".format(N))
        f.write("Sum: {:.2f}\n".format(sum(numbers)))
        f.write("Avg: {:.2f}\n".format(sum(numbers)/N))
        f.write("Min: {:.2f}\n".format(min(numbers)))
        f.write("Max: {:.2f}\n".format(max(numbers)))

if __name__ == "__main__":
    numbers = ask_number()
    sort_results(numbers)
    write_results(numbers, len(numbers))

