import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3','4','5','6','7','8','9']

symbols = ['!', '#', '$', '%','&',')','(','+','*']

print("Welcome to the PyPassword Generator!")

in_letters = int(input("how many letters would you like in your password?\n"))
in_symbols = int(input("how many symbols would you like in your password?\n"))
in_numbers = int(input("how many numbers would you like in your password?\n"))

# easy level
# fgfh^&23
# password = ""
# for char in range(1,in_letters +1):
#     password += random.choice(letters) 
  
# for sys in range(1,in_symbols+1):
#     password += random.choice(symbols)

# for num in range(1,in_numbers+1):
#     password += random.choice(numbers)

# print(password)    

# hard level
# g^2jk8&
password_list = []
for char in range(1,in_letters +1):
    password_list += random.choice(letters) 
  
for sys in range(1,in_symbols+1):
    password_list += random.choice(symbols)

for num in range(1,in_numbers+1):
    password_list += random.choice(numbers)

# print(password_list) 
random.shuffle(password_list)
# print(password_list)

# converting list to string
password = ""
for char in password_list:
    password +=char
print(f"your password is {password}")    


    