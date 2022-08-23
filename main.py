from replit import clear

from art import logo

print(logo)

bids = {}
bidding_finish = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid amount of ${highest_bid}")


while not bidding_finish:
    name = input("What is your name?\n")
    price = int(input("What is your Bid?\n$"))
    bids[name] = price
    s_continue = input("Are there any other bidders?Type 'yes'or'no'\n ")
    if s_continue == "no":
        bidding_finish = True
        find_highest_bidder(bids)

    elif s_continue == "yes":
        clear()
