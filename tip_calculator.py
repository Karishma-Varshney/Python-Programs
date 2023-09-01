# concept of arithematic operations

# 12/100
# 0.12
# 150*0.12
# 18
# 150+18
# 168
# 168/5
# 33.6

# FIRST METHOD
print("Welcome to the tip calculator.")
amount = float(input("What was the total bill?"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
tip_percent = 1+tip/100
new_amount = amount * tip_percent
people = int(input("How many people to split the bill?"))
pay = round(new_amount/people,2)
print(f"Each person should pay: {pay} " )


# SECOND METHOD
print("Welcome to the tip calculator.")
amount = float(input("What was the total bill?"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
a = tip/100
b = amount * a
c = amount + b
people = int(input("How many people to split the bill?"))
pay = round(c/people,2)
print(f"Each person should pay: {pay} " )