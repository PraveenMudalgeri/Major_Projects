import random
import os
from art import logo11

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if len(cards) == 2 and sum(cards) == 21: #blackjack
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards[cards.index(11)] = 1  #or use [cards.remove(11) cards.append(1)]
    return sum(cards)

def compare(user_score, computer_score):
    #Bug fix. If you and the computer are both over, you lose.
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    
    if user_score == computer_score:
        return "It's a draw! 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return 'Win with a Blackjack 😎'
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁" 
    else:
        if user_score > computer_score:
            return "You win 😃"
        else:
            return "You lose 😤"

def restart_game():
    restart = input('Do you want to restart the game? Type "y" or "n": ').lower()
    if restart == 'y':
        os.system('cls')
        return True
    else:
        os.system('cls')
        print("Bye! Have a great day.👋")
        return False

def play_game():
    while True:
        print(logo11)
        
        user_cards = [deal_card(), deal_card()]
        computer_cards = [deal_card(), deal_card()]
        print(f'Your cards are : {user_cards}')
        print(f'Computer\'s first card is : {computer_cards[0]}')

        computer_score = calculate_score(computer_cards)
        user_score = calculate_score(user_cards)
        
        continue_play = True
        while continue_play:  
            user_score = calculate_score(user_cards)
            print(f'Your score is : {user_score}')
            if user_score == 0 or computer_score == 0 or user_score > 21:
                continue_play = False
            else:
                draw_card = input('Do you want to draw another card? Type "y" or "n": ').lower()
                if draw_card == 'y':
                    user_cards.append(deal_card())
                else:
                    continue_play = False
        
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card()) 
            computer_score = calculate_score(computer_cards)
        
        print(f'Computer\'s cards are {computer_cards} and score is {computer_score}')
        print(compare(user_score, computer_score))
        
        if not restart_game():
            break


play_game()