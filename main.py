############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random
from art import logo
import os


# Create a deal_card() function to return a random card from the deck. 11 is the ACE

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# Create a calculate_score() function to calculate the sum value of cards

def calculate_score(cards):
    # Check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


# Create a compare() function that takes in user score and computer score then compare the scores
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "DRAW"
    elif computer_score == 0:
        return "YOU LOSE! Opponent has Black Jack"
    elif user_score == 0:
        return "YOU WIN with a Black Jack"
    elif user_score > 21:
        return "YOU LOSE! You went over"
    elif computer_score > 21:
        return "YOU WIN! Opponent went over"
    elif user_score > computer_score:
        return "YOU WIN!"
    else:
        return "YOU LOSE!"


# Create a play_game() function to automate and repeat the game if user wants to continue to play
def play_game():

    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal the user and computer 2 cards each using deal_card() and append().
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # The score will need to be rechecked with every new card drawn and the checks need to be repeated until the game ends.
    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")
        print("-----------------------------------------------")

        # If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print("-----------------------------------------------")
    print(f"   {compare(user_score, computer_score)}")


# Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack
while input("Do you want to play BlackJack? Type 'y' or 'n': ") == 'y':
    os.system('clear')
    play_game()
