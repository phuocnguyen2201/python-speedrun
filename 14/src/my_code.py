# -*- coding: utf-8 -*-


def main():
    from random import choice
    N = int(input("How many numbers? "))
    if N < 1:
        print("Error!")
    else:
        numbers = [choice(range(0, 21, 2)) for _ in range(N)]
        print(f"Min and max: {min(numbers)},{max(numbers)}")
        for i in range(N):
            if i == N - 1:
                print(numbers[i])
            else:
                print(numbers[i], end=",")

main()