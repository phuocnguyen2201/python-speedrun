# -*- coding: utf-8 -*-

def main():
    language = input("Please choose language (0 = suomi, 1 = english): ")
    if language != "0" and language != "1":
        language = "0"
    
    days = []
    if language == "0":
        days = ["maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai"]
    else:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    rain = {}
    for day in days[:5]:
        rain[day] = []
        for i in range(4):
            rain[day].append(float(input(f"{day} {i+1}. : ")))
    
    for day in days[:5]:
        print(f"{day} {sum(rain[day])/len(rain[day]):.1f} mm")
        
main()