

#Call this  function to read integer from the user
#Reads an integer from the keyboard and shows msg.
#If given string is not valid integer a new one will be asked
def input_int(msg):
    while True:
        try:
            return int(input(msg))
        except:
            pass



#Write your functions here!
def ask_grades():
    
    name = input("Name : ")
    grade = input_int("Grade : ")
    grades = {}

    while True:
        if grade < 0:
            grade = 0
        if grade > 5:
            grade = 5
        grades[name] = grade
        name = input("Name : ")
        if name == "END":
            break
        grade = input_int("Grade : ")

    return grades

def print_failed(grades):

    count_failed = failed_count(grades)
    if count_failed > 0:
        print(f"There are {count_failed} failed students.")
        for name, grade in grades.items():
            if grade == 0:
                print(name, grade)
                
    else:
      print_grades(grades)

def failed_count(grades):
    failed_students = []

    for name, grade in grades.items():
        if grade == 0:
            failed_students.append(name)
    return len(failed_students)

def print_grades(grades):

    for name, grade in grades.items():
        print(name, grade)
        
if __name__ == "__main__":
    #Write main program below this line
    grades = ask_grades()
    print_failed(grades)
        
