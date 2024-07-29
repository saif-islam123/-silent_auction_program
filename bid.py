import os

def clear_screen():
    if should_continue == 'yes':
        os.system("cls")

print("Welcome to the secret bidding system:")

bids = {}
while True:
    name = input("What is your name? ")
    bid = int(input(f"What is your bid? $"))
    bids[name] = bid
    should_continue = input("Is there any bidder left? 'yes' or 'no' ")
    if should_continue == 'no':
        break
    clear_screen()

greater_bid = 0
winner = ""
for name, bid in bids.items():
    if bid > greater_bid:
        greater_bid = bid
        winner = name
        
print(f"Thw winner is {winner} with the bid of ${greater_bid}")
    
