# concept of f string

age = input("enter your current age : ")
life_left = 90-int(age)
# print(life_left)
# x for days
x = life_left * 365
# y for weeks
y = life_left * 52
# z for months
z = life_left * 12

print(f"You have {x} days, {y} weeks, and {z} months left.")
