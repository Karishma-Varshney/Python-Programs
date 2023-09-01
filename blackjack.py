logo = """
                        _____
                       |A _  | _____
                       | ( ) ||A_ _ |
                       |(_'_)||( v )|
                       |  |  || \ / |
                       |____V||  .  |
                              |____V| 

 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ \t
                       _/ |                 
                      |__/                     """

import random
import os

def deal_card():
    """returns a random card from the deck/list"""
    num_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(num_list)
    return card

def calculate_score(card):
    """takes a list and returns the sum"""
    if sum(card)==21 and len(card)==2:
        return 0
    if 11 in card and sum(card)>21:
        card.remove(11)
        card.append(1)

    return sum(card)

def compare(user_score,comp_score):
    if user_score == comp_score:
        return "draw"
    elif comp_score == 0:
        return "you lose, opponent has blackjack"
    elif user_score == 0:
        return "win with a blackjack"
    elif user_score>21:
        return "you went over.you lose."
    elif comp_score>21:
        return "opponent went over.you win."
    elif user_score>comp_score:
        return "you win"
    else:
        return "you lose"    
    
def play_game():
    print(logo)
    print("welcome to the blackjack game.")
    comp = []
    user = []
    is_game_over = False
    for _ in range(2):
        user.append(deal_card())
        comp.append(deal_card())
    while not is_game_over: 
        user_score = calculate_score(user)  
        comp_score = calculate_score(comp) 
        print(f"your cards: {user}, current score: {user_score}")
        print(f"computer first card: {comp[0]}") 

        if user_score == 0 or comp_score == 0 or user_score>21:
            is_game_over = True
        else:
            x = input("type 'y' to get another card, type 'n' to pass: ").lower()
            if (x =='y'):
                user.append(deal_card())
            else:
                is_game_over = True   

        while comp_score != 0 and comp_score>17:
            comp.append(deal_card())   
            comp_score = calculate_score(comp) 

    print(f"your final hand: {user} , your final score:{user_score}")       
    print(f"computer final hand: {comp} , computer final score:{comp_score}")       

    print(compare(user_score,comp_score))

while input("do you want to play the game? type 'y' or 'n' : ") == 'y':
     os.system('cls')
     play_game()



    # if(x == 'y'):
    #     c3 = random.choice(num_list)
    #     second_score = first_score+c3
    #     user.append(c3)
    #     print(f"your cards: {user}, final score: {second_score}")
    #     comp2 = random.choice(num_list)
    #     comp.append(comp2)
    #     result = comp1+comp2
    #     if (result<17):
    #         comp3 = random.choice(num_list)
    #         comp.append(comp3)
    #         oth_result = comp3+result
    #         print(f"computer final card: {comp}, final score: {oth_result}")
    #     else:
    #         print(f"computer final card: {comp}, final score: {result}")

    # elif (x == 'n'):
    #     comp2 = random.choice(num_list)
    #     comp.append(comp2)
    #     result = comp1+comp2
    #     if (result<17):
    #         comp3 = random.choice(num_list)
    #         comp.append(comp3) 
    #         oth_result = comp3+result
    #         print(f"computer final card: {comp}, final score: {oth_result}")
    #     else:
    #         print(f"computer final card: {comp}, final score: {result}")





