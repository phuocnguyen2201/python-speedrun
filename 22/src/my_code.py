# -*- coding: utf-8 -*-
def ask_name():
    name = input("Give your name : ")
    if len(name) > 18:
        print("Error!")
        return
    
    length = len(name)
    name = name[::-1]

    for i in range(length):
        print(" " * (length - i - 1) + name[i])

    with open("name.txt", "w") as f:
        for i in range(length):
            f.write(" " * (length - i - 1) + name[i] + "\n")


if __name__ == "__main__":
    ask_name()