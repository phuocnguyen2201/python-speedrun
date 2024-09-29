
#Write functions and define global variables here!
def check(*args):
    print(f"Number of arguments: {len(args)}")
    if len(args) == 0:
        print("Error!")
        return
    if args[0] == "teacher":
        print("Teaching programming!")
    elif args[0] == "student":
        print("Learning programming!")
    else:
        print("I don't understand!")


if __name__ == "__main__":
    #Write main program below this line
    check()
