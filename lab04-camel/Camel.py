import random
import arcade

def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down!"
          " Survive your desert trek and out run the natives.")
    done = False
    milestrav = 0
    thirst = 0
    cameltired = 0
    nativedist = -20
    distnative_you = milestrav - nativedist
    canteendrinks = 3
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
        elif user_choice.upper() == "E":
            print(milestrav)
            print(canteendrinks)
            print(distnative_you)
        elif user_choice.upper() == "D":
            print("The camel is happy")
            distrandom = random.randint(7, 14)
            nativedist = nativedist + distrandom
        elif user_choice.upper() == "C":
            distrandom2 = random.randint(10, 21)
            milestrav = milestrav + distrandom2
            print("You traveled ",distrandom2)
            thirst = thirst + 1
            tirenessrandom = random.randint(1, 3)
            cameltired = cameltired + tirenessrandom
            distrandom = random.randint(7, 14)
            nativedist = nativedist + distrandom
            if random.randrange(20) == True:
                print("You found an oasis")
                canteendrinks = 3
                thirst = 0
                cameltired = 0
        elif user_choice.upper() == "B":
            distrandom2 = random.randint(5, 12)
            milestrav = milestrav + distrandom2
            print("You traveled ",distrandom2)
            thirst = thirst + 1
            cameltired = cameltired + 1
            distrandom = random.randint(7, 14)
            nativedist = nativedist + distrandom
            if random.randrange(20) == True:
                print("You found an oasis")
                canteendrinks = 3
                thirst = 0
                cameltired = 0
        elif user_choice.upper() == "A":
            if canteendrinks != 0:
                canteendrinks = canteendrinks - 1
                thirst = 0
            else:
                print("ERROR")
        if 6 >= thirst > 4:
            print("You are thirsty")
        elif thirst > 6:
            print("You died of thirst!")
            done = True
        if 8 >= cameltired > 5:
            print("Your camel is getting tired")
        elif cameltired > 8:
            print("Your camel is dead")
            done = True
        if distnative_you == 0:
            print("The natives caught you")
            done = True
        elif distnative_you < 15:
            print("The natives are getting close")
        if milestrav >= 200:
            if done == False:
                print("You've won!!")
                done = True






main()
