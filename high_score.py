# creating list using split method

std_scores = input("input list of student score ").split()
for n in range(0,len(std_scores)):
    std_scores[n] = int(std_scores[n])
print(std_scores) 
x = 0
for score in std_scores:
    if score>x:
        x=score
print(f"the highest score is : {x}")        

