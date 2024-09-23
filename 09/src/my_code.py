# -*- coding: utf-8 -*-

def NUMBER_TO_GUESS():
    return 124
  
def main():
    number = NUMBER_TO_GUESS()
    guess = 0
    count = 0
    while guess != number:
        guess = int(input("Give a positive integer: "))
        count += 1
        if guess < number:
            print("Your guess was too small")
        elif guess > number:
            print("Your guess was too big")
    print(f"You guessed the value by {count} guesses! Nice!")
    
main()