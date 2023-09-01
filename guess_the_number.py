
logo = """ 
                                          __   __                                          __               
   ____ _ __  __ ___   _____ _____       / /_ / /_   ___         ____   __  __ ____ ___   / /_   ___   _____
  / __ `// / / // _ \ / ___// ___/      / __// __ \ / _ \       / __ \ / / / // __ `__ \ / __ \ / _ \ / ___/
 / /_/ // /_/ //  __/(__  )(__  )      / /_ / / / //  __/      / / / // /_/ // / / / / // /_/ //  __// /    
 \__, / \__,_/ \___//____//____/       \__//_/ /_/ \___/      /_/ /_/ \__,_//_/ /_/ /_//_.___/ \___//_/     
/____/                                                                                                          

  """

import random
import os

print(logo)
print("welcome to the Number guessing game.")

game_on = True


while game_on:
  n = random.randint(1,100)
  i = input("choose a difficulty . type 'easy' or 'hard' :")

  def easy():
      j=10
      while(j>0):
          print(f"u have {j} attempts remaining to guess the number.")
          z = int(input("make a guess: "))
          if(z==n):
              print(f"you got it!!\nthe answer was {z}.")
              y = input("do you want to play again. type 'yes' or 'no' :").lower()
              if y=='yes':
                 break
              else:
                  print("ty")
              break
          elif(z>n):
              print("too high.")
              j -=1
          else:
              print("too low.")
              j -=1 

      # if there is no attempts left           
      if(j==0):
        print("you lose.") 
        y = input("do you want to play again. type 'yes' or 'no' :").lower()
        if y=='yes':
             game_on = True
        else:
             game_on = False
             print("come back soon!!!")
             
      

  def hard():
      j=5
      while(j>0):
          print(f"u have {j} attempts remaining to guess the number.")
          z = int(input("make a guess: "))
          if(z==n):
              print(f"you got it!!\nthe answer was {z}.")
              y = input("do you want to play again. type 'yes' or 'no' :").lower()
              if y=='yes':
                 break
              else:
                  print("ty")
              break
          elif(z>n):
              print("too high.")
              j -=1
          elif(z<n):
              print("too low.")
              j -=1 

 # if there is no attempts left
      if(j==0):
          print("you lose.") 
          y = input("do you want to play again. type 'yes' or 'no' :").lower()
          if y=='yes':
             game_on = True
          else:
             game_on = False
             print("come again!!!")
             

# user choice made either easy or hard level
  if(i=="easy"):
    easy()
  else:
    hard()

     



      
              

                
            
            
    
