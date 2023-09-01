import os

logo = '''              
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\ \t
                         `'-------'`
                       .-------------.
                      /_______________\      '''

print(logo)
print("Welcome to Secret Auction ")
bid = {}
bidding_finished = True


# function for highest bidder
def highest_bidder(bidding_record):
    highest_amount = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount>highest_amount:
            highest_amount = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of Rs.{highest_amount}")        



while bidding_finished:
    
    Name = input("What's your name : ")
    amount = int(input("what's your bid : Rs."))

    bid[Name] = amount
    
    n = input("Did someone else want to bid ? type 'yes' or 'no': ").lower()
    if (n=='yes'):
        bidding_finished = True
        os.system('cls')
    elif n=='no':
        bidding_finished = False
        highest_bidder(bid)

    else:
        print("enter a valid choice.")
        bidding_finished = False

# print(bid)    



               
