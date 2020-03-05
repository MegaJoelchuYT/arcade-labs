def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down!"
          " Survive your desert trek and out run the natives.")
    done = False
    while done == False:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        user_choice = str(input("What is your choice? "))
        if user_choice.upper() == "Q":
            print("You have quit the game")
            done = True

main()
