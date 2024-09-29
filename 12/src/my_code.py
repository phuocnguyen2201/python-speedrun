# -*- coding: utf-8 -*-


def main():
    child_benefit = 0
    total_benefit = 0
    while True:
        new_data = input("New data (y/n): ")
        if new_data == "n":
            break


        solitaire_or_cohabit = int(input("Solitaire (1) or cohabit (2): "))
        if solitaire_or_cohabit == 1:
            base_amount = 16.18
        elif solitaire_or_cohabit == 2:
            base_amount = 13.76
       
        underage_children = input("Any underage children (y/n): ")

        if underage_children == "y":
            children_less_than_10   = int(input("Children less than 10 years: "))
            children_10_17          = int(input("Children 10-17 years: "))
            child_benefit           = (children_less_than_10 * 10.20) + (children_10_17 * 11.33)
            if(children_10_17 + children_less_than_10 > 1):
                base_amount         = 17.80

        elif underage_children == "n":
            total_benefit = base_amount

        days = int(input("Days: "))

        total_benefit = (base_amount * days) + (child_benefit * days)
        print(f"Amount of the benefit is {total_benefit:.2f} euro")

main()