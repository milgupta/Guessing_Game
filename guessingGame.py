import random

play = input("Hello, this is a guessing game would you like to play?  (Yes or no)\n\n")


if play == "Yes":
    difficulty = int(input("\nWelcome, choose the difficutly as either 1 (easy) or 2 (hard)\n\n"))
    if difficulty == 1:
        tries = 20
        number = random.randint(1,250)
        print("\nNow choose a number between 1 - 250")
        while tries > 0:

            guess = int(input("\n"))

            if guess == number:
                print("\nWell done, you found the number. ")
                print("")
                break

            elif guess < number:
                print("\nNumber too low, try again. You have " + tries + " remanining.")

            elif guess > number:
                print("\nNumber too high, try again. You have " + tries + " remanining.")
            
            tries-=1
            
    else:
        tries = 10
        number = random.randint(1,500)
        print("\nNow choose a number between 1 - 500")
        while tries > 0:

            guess = int(input("\n"))

            if guess == number:
                t = 10 - int(tries)
                print("\nWell done, you found the number in " + str(t))
                print("    _______")
                print(" _//_||_\\_")
                print("| _  ..  _ |")
                print("'-(_)--(_)-'")
                break

            elif guess < number:
                print("\nNumber too low, try again. You have " + tries + " remanining.")

            elif guess > number:
                print("\nNumber too high, try again. You have " + tries + " remanining.")
            
            tries-=1

else:
    print(""" LOSER
   ____        _   _                 
  / ___| _ __ | |_(_)_ __   __ _ ___ 
 | |  _ | '_ \| __| | '_ \ / _` / __|
 | |_| || | | | |_| | | | | (_| \__ \\
  \____||_| |_|\__|_|_| |_|\__, |___/
                          |___/      
""")