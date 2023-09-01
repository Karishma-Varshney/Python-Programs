import os

logo = """ 
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________| 

       _..._                          _..._                                      .-'''-.             
    .-'_..._''.           .---.    .-'_..._''.         .---.                    '   _    \           
  .' .'      '.\          |   |  .' .'      '.\        |   |                  /   /` '.   \          
 / .'                     |   | / .'                   |   |                 .   |     \  '          
. '                       |   |. '                     |   |              .| |   '      |  '.-,.--.  
| |                 __    |   || |                     |   |    __      .' |_\    \     / / |  .-. | 
| |              .:--.'.  |   || |              _    _ |   | .:--.'.  .'     |`.   ` ..' /  | |  | | 
. '             / |   \ | |   |. '             | '  / ||   |/ |   \ |'--.  .-'   '-...-'`   | |  | | 
 \ '.          .`" __ | | |   | \ '.          .' | .' ||   |`" __ | |   |  |                | |  '-  
  '. `._____.-'/ .'.''| | |   |  '. `._____.-'/  | /  ||   | .'.''| |   |  |                | |      
    `-.______ / / /   | |_'---'    `-.______ /   `'.  |'---'/ /   | |_  |  '.'              | |      
             `  \ \._,\ '/                  `'   .'|  '/    \ \._,\ '/  |   /               |_|      
                 `--'  `"                     `-'  `--'      `--'  `"   `'-'                           """


print(logo)
def add(n1,n2):
        return n1+n2

def sub(n1,n2):
        return n1-n2

def multiply(n1,n2):
        return n1*n2

def divide(n1,n2):
        return n1/n2
operation = {
        
        "+" : add,
        "-" : sub,
        "*" : multiply,
        "/" : divide,
        
        }
def calculate():   
    n1 = float(input("what's first number? : "))
    for symbol in operation:
        print(symbol)

    should_continue = True
    while should_continue:

        o = input("pick an operation : ")
        n2 = float(input("what's next number? : "))
        calculation_function = operation[o]
        first_answer = calculation_function(n1,n2)
        print(f"{n1} {o} {n2} = {first_answer}")

        x = input("type 'y' to continue, or type 'n' to start a new calculation: ").lower()

        if ( x == 'y'):
            n1 = first_answer
        elif (x == 'n'):
              os.system('cls')
              calculate()
              
calculate()              

            
            
    
 
        

    

