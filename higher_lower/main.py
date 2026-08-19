# Display art
import random
from art import logo,vs
from game_data import data

# Create the functions
def formart_data(account):
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


print(logo)
score = 0
should_continue = True
account_b = random.choice(data)
# Generate a random account from the game data

while should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A {formart_data(account_a)}")
    print(vs)
    print(f"Against B {formart_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(logo)

    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']

    is_correct = check_answer(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"Correct! You got it in {score} guesses!")
    else:
        print(f"Sorry, that's wrong. You got it in {score} guesses!")
        should_continue = False
