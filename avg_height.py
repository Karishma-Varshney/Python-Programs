# gives a average of height in a list

std_height = input("input list of student height ").split()
for n in range(0,len(std_height)):
    std_height[n] = int(std_height[n])
print(std_height) 

sum = 0
count = 0

for height in std_height:
    sum = sum + height
    count = count + 1
average = round(sum/count) 
print(average)
    