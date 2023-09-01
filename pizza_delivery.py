print("Welcome to Python pIzza Deliveries!")
bill = 0

size = input("what size pizza do you want? S, M or L ")
add_pepperoni = input("do you want pepperoni? Y or N ")
if size == "S":
    if add_pepperoni == "Y":
        bill = 17
    else:
        bill = 15    
    
elif size == "M":
    if add_pepperoni == "Y":
        bill = 23
    else:
        bill = 20    
else:
    if add_pepperoni == "Y":
        bill = 28
    else:
        bill = 25    


extra_cheese = input("do you want extra cheese? Y or N ") 
if extra_cheese == "Y":
    bill += 1

print(f"your final bill is: $ {bill}")       
