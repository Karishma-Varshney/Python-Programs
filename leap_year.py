
# FIRST METHOD
year = int(input("enter year of your choice : "))
if(year%4==0 & year%400 ==0):
    print("leap year")
else:    
    print(" non leap year")


# SECOND METHOD
year = int(input("enter year of your choice : "))
if(year%4==0):
    if year%100 == 0:
        if year%400 == 0:
            print("leap year")
        else:
            print("not leap year")    
    else:
        print("leap year")        
    
else:    
    print(" not leap year")

    
