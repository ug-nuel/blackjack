import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    random_integer = random.choice(cards)
    return random_integer


def calculate_score(cards):
    ''' take a list of cards and return the score calculated from the cards'''
    total = sum(cards)
    card_length = len(cards)
    if total == 21 and card_length == 2:
        return 0
    elif 11 in cards and total > 21:
        cards.remove(11)
        cards.append(1)
    else:
        return total


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "its a draw"
    elif user_score == 0:
        return "Win with a blackjack"
    elif computer_score == 0:
        return "Lose, opponent has a blackjack"
    elif user_score > 21:
        return "you went over, you lose"
    elif computer_score > 21:
        return "opponent went over, you win"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"


def play_game():
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_end = False
    while not game_end:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")
        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_end = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                game_end = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand: {user_cards}, final score: {user_score}")
    print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of blackjack? type 'y' or 'n': ") == 'y':
    os.system('cls')
    play_game()
