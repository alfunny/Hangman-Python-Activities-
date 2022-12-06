from replit import clear
# OBS: I maid the code in replit,so i imported the clear method to use . Other option is to create a clear function to clean the console
import art


leilao = {}
verificator = True
print(art.logo)
while verificator:
    name = input("What's your name?\n")
    bid = input("what's your bid?\n")
    leilao[name] = bid
    continue_bid = input("Are there any other bidders? Type 'yes or 'no'\n")
    clear()
    if continue_bid == 'no':
        verificator = False

biggest_bid = " "
index = " "
for bidder in leilao:
    if biggest_bid < leilao[bidder]:
        biggest_bid = leilao[bidder]
        index = bidder


print(f"The winner is {index} with a bid of ${biggest_bid}")
