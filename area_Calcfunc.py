# rounding UP number in python by importing math module and using math.ceil(<number>)

import math
def area_calc(h,w,c):
    print(f"height of wall is {h}")
    print(f"width of wall is {w}")
    print(f"coverage per can is {c}")
    # number of cans = (height of wall*width of wall)/coverage

    number_of_cans = (h*w)/c
    print(number_of_cans)
    approx_cans = math.ceil(number_of_cans)
    print(f" you'll require {approx_cans} cans")

h = int(input("enter height of wall: ")) 
w = int(input("enter width of wall: ")) 
c = int(input("enter coverage per can: ")) 
area_calc(h,w,c) 


