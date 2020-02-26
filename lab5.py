import random

def main():

    def print_intro():
        print("Welcome to the Camel!")
        print(""" In your desperation, you have a stolen camel to make your way 
        across the great Mobi desert.
        The locals want their camel back and are chasing you down!
        Survive your desert trek and out run the locals.""")
    
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    locals_traveled = -20
    canteen = 3
    done = False

    while not done:
         nativesBehind = miles_traveled - locals_traveled
    fullSpeed = random.randrange(10, 21)
    moderateSpeed = random.randrange(5, 13)
    print("""
    A. Drink from your canteen.
    B. Ahead at moderate speed.
    C. Ahead full speed.
    D. Stop for the night.
    E. Status check
    Q. Quit.""")
    print()
    userInput = input("Your choice? ")
    if userInput.lower() == "q":
            done = True

#status
    elif userInput.lower() == "e":
        print("Miles traveled: ",miles_traveled)
        print("Drinks in canteen: ",canteen)
        print("Your camel has ",camel_tiredness,"amount of tiredness.")
        print("The natives are ",nativesBehind,"miles behind you.")
#stop for night
    elif userInput.lower() == "d":
        camel_tiredness *= 0
        print("Your camel feels refreshed and happy his tiredness is now ",camelFatigue)
        locals_traveled += random.randrange(7, 15)
#move full speed
    elif userInput.lower() == "c":
        print("You traveled ",fullSpeed,"miles!")
        miles_traveled += fullSpeed
        thirst += 1
        camel_tiredness += random.randrange(1, 4)
        locals_traveled += random.randrange(7, 15)
        oasis = random.randrange(1, 21)

#move moderate speed
    elif userInput.lower() == "b":
        print("You traveled ",moderateSpeed,"miles!")
        miles_traveled += moderateSpeed
        thirst += 1
        camel_tiredness += 1
        locals_traveled += random.randrange(7, 15)
        oasis = random.randrange(1, 21)

        #drink canteen
    elif userInput.lower() == "a":
        if canteen == 0:
            print("You're out of water.")
        else:
            canteen -= 1
            thirst *= 0
            print("You have ",canteen,"drinks left and you are no longer thirsty.")

#not done check
    if oasis == 20:
        camel_tiredness *= 0
        thirst *= 0
        canteen = 3
        print("You found an oasis! After taking a drink you filled your canteen and the camel is refreshed.")
    if nativesBehind <= 15:
        print("The natives are drawing near!")
    if miles_traveled >= 200 and not done:
        print("You made it across the desert, you win!")
        done = True
    if locals_traveled >= miles_traveled:
        print("The locals caught and beheaded you.")
        print("You're dead!")
        done = True
    if thirst > 4 and thirst <= 6 and not done:
        print("You are thirsty")
    if thirst > 6:
        print("You died of dehydration!")
        done = True
    if camel_tiredness > 5 and camel_tiredness <= 8 and not done:
        print("Your camel is getting tired.")
    if camel_tiredness > 8:
        print("Your camel is dead.")
        done = True

if __name__ == "__main__":
    main()