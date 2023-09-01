name1 = input("enter first name: ")
name2 = input("enter second name: ")
a = name1.lower()
b = name2.lower()

combined_name = a + b 

T = combined_name.count("t")
R = combined_name.count("r")
U = combined_name.count("u")
E = combined_name.count("e")
total1 = T+R+U+E

L = combined_name.count("l")
O = combined_name.count("o")
V = combined_name.count("v")
E = combined_name.count("e")
total2 = L+O+V+E

love_score = str(total1) + str(total2)
score = int(love_score)

if score<10 or score>90:
    print("your score is " + love_score + ", you go together like coke and mentos.")
elif score>=40 and score<=50:
    print("your score is " + love_score + ", you are alright together.")
else:
    print("your score is " + love_score)        

