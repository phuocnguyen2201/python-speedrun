

#Implement AskAndTest function here!
def AskAndTest():
    user_input = input("Give an integer: ")
    number = int(user_input)
    #print(number)
    if number > 0:
        return 1
    elif number == 0:
        return 0
    elif number < 0:
        return -1
    else:
        return "Error!"


if __name__ == "__main__":
    #Write main program below this line
   while True:
      result = AskAndTest()
      if result == 1:
         print("Positive")
      elif result == 0:
         print("Zero")
      elif result == -1:
         print("Negative")
      else:
         print("Error!")
         
         
         
      
      
