
#Write functions, define global variables, and import modules here!
import datetime

def ask_cars():

   numbers = {}

   while True:

      number = input("Registration number : ")
      if number == "END":
            break
      date = input("Registration date: ")

      while True:
            try:
               datetime.datetime.strptime(date, "%d.%m.%Y")
               break
            except ValueError:
               print("Error: Give date in format dd.mm.yyyy : ", end="")
               date = input()
      numbers[number] = date
   return numbers

def save_cars(d):
   with open("cars.txt", "w") as f:
      for key, value in d.items():
         f.write(f"{key}\t{value}\n")

def read_cars():
   numbers = {}
   with open("cars.txt") as f:
      for row in f:
         key, value = row.strip().split("\t")
         numbers[key] = value
   return numbers

def print_data(d):
   for key, value in d.items():
      print(key, value)
if __name__ == "__main__":
    #Write main program below this line
    numbers = ask_cars()
    save_cars(numbers)
    print_data(read_cars())
    


