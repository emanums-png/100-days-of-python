import art

print(art.logo)

bids = {}

while True:
    name = input('What is your name?\n')
    bid = int(input('What is your bid? $\n'))
    bids[name] = bid
    add_user = input('There are other users who want to bid?\n').lower()

    if add_user == 'no':
        print('\n' * 20)
        break
    else:
        print('\n' * 20)

highest_bid = 0
winner = ''

for name in bids:
    if bids[name] > highest_bid:
        highest_bid = bids[name]
        winner = name

print(f'The winner is {winner} with a bid of ${highest_bid}')
