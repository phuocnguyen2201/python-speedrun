# -*- coding: utf-8 -*-

def main():
    
    S = int(input("Start: "))
    N = int(input("Steps: "))
    
    for i in range(N):
        print(f"{S+i},{S-i}")
        
main()