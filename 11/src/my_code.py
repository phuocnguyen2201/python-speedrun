# -*- coding: utf-8 -*-

def main():
    
    import math
    
    radius = 0
    
    while True:
        print("0 = Exit")
        print("1 = Give radius")
        print("2 = Compute circumference of the circle")
        print("3 = Compute area of the circle")

        selection = int(input("Select: "))
        
        if selection == 0:
            break
        elif selection == 1:
            radius = float(input("Give radius: "))
        elif selection == 2:
            print(f"Circumference is {2*math.pi*radius:.2f}")
        elif selection == 3:
            print(f"Area is {math.pi*radius**2:.2f}")
        else:
            break
        
main()



