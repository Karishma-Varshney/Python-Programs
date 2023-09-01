print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

choice1 = input("what will you choose? left or right ? \n").lower()
if choice1 == "right":
    print("Game Over")
else:
    choice2 = input("do you want to swim or wait? \n").lower()
    if choice2 == "swim":
        print("game over")
    else:
        choice3 = input("which color would you choose ? red, blue or yellow? \n").lower() 
        if choice3 == "red":
            print("game over")
        elif choice3 == "blue":
            print("game over")
        else:
            print("you win!!!")              