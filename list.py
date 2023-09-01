import random

names_string = input("give me everybody's names. ")

# it will make a list of names
names = names_string.split(",")
print(names)

# we can also use random.randint(0,len(names)-1)
# or we can simply use random.choice(names) which chooses random things from a sequence like list
random_idx = random.randrange(len(names))
# print(random_idx)

payer = names[random_idx]
print(f"{payer} is going to buy the meal today!")




