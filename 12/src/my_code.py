# -*- coding: utf-8 -*-


def main():
    while True:
        
        solitaire = int(input("Solitaire (1) or cohabit (2): "))
        underage = input("Any underage children (y/n): ")
        
        if underage == "y":
            children_less_than_10 = int(input("Children less than 10 years: "))
            children_10_17 = int(input("Children 10-17 years: "))
        else:
            children_less_than_10 = 0
            children_10_17 = 0
        days = int(input("Days: "))
        if solitaire == 1:
            amount = 16.18
        else:
            amount = 13.76 * 2
            
        amount += 11.33 * children_10_17 + 10.20 * children_less_than_10
        
        print(f"Amount of the benefit is {amount * days:.2f} euro")
        if input("New data (y/n): ") == "n":
            break
        
main()