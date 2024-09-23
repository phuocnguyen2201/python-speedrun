

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
    students = {}
    
    while True:
        if grade < 0:
            grade = 0
        if grade > 5:
            grade = 5
        students[name] = grade
        name = input("Name : ")
        if(name == "END" or name == "Bad input"):
            return students
        grade = input_int("Grade : ")
    return students
  
def print_failed(grades):
  
    failed = []
    
    for name, grade in grades.items():
        if grade == 0:
            failed.append(name)
    print("There are", len(failed), "failed students.")
    for name in failed:
        print(name, 0)
        
def failed_count(grades):
    failed = 0
    for name, grade in grades.items():
        if grade == 0:
            failed += 1
    return failed
  
def print_grades(grades):
    for name, grade in grades.items():
        print(name, grade)
        
if __name__ == "__main__":
    #Write main program below this line
    grades = ask_grades()
    failed = failed_count(grades)
    if failed > 0:
        print_failed(grades)
    else:
        print_grades(grades)
        
