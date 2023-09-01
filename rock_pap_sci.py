import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")


paper =("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")


scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors) 
else:
    print("enter valid choice")    

print("computer chose:")

comp = random.randint(0,2)
if comp == 0:
    print(rock)
elif comp == 1:
    print(paper)
else:
    print(scissors) 

# rock wins over scissors
# paper wins over rock
# scissors wins over paper
if choice == comp:
    print("draw!!")
elif choice==0 and comp==2:
    print("you win!!")   
elif choice==1 and comp==0:
    print("you win!!")   
elif choice==2 and comp==1:
    print("you win!!")  
else:
    print("you lose!!")  

