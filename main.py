from replit import clear
import art

print(art.logo)
print("Welcome to the secret auction program.")
run_loop = True
user_bid_dictionary = {}

while run_loop:
  user_name = input("What is your name?: ")
  user_bid = int(input("What's your bid?: $"))
  user_response = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  user_bid_dictionary[user_name] = user_bid
  if user_response == "yes":
    clear()
  else:
    run_loop = False

def find_highest_bidder(bidding_record):
  winner = ""
  bid = 0
  for key in bidding_record:
    if bidding_record[key] > bid:
      winner = key
      bid = bidding_record[key]
  print(f"The winner is {winner} with a bid of ${bid}")

find_highest_bidder(user_bid_dictionary)
