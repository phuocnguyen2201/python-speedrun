# -*- coding: utf-8 -*-


grade = int(input("Give grade (0-5): "))

while True:
    if (0 <= grade <= 5):
        if (grade >= 4):
            print("Excellent")
        elif (grade >=3):
            print("Good")
        elif (grade >= 1):
            print("Passed")
        else:
            print("Not passed")
    else:
        print("Invalid grade!")
    grade = int(input("Give grade (0-5): "))

    