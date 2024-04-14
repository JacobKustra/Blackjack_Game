"""
Your Name: Jacob Kustra
Class: CS 521 - Fall 2022
Date: 11/16/22
Blackjack Game
Description of Problem (1-2 sentence summary in your own words):
My Final Project for MET CS 521 is a functioning game of Blackjack which starts the player
off with 1000 tokens and allows them to play until they lose it all or decide to stop.
"""


import random
import copy
import sys
import time
from Player_Class import *

# Game Initialization
name = input("Please enter your name: ").strip().capitalize()
player1 = Player(name)  # Initializes Player class methods

# Building Card Deck
all_cards = open("Cards.txt", "r")  # Opens and reads text file containing card names and values.
card_dict = dict()
card_list = []
copy_of_card_list = []

for card in all_cards:  # Takes cards from text file and puts them into a dictionary and list.
    card = card.replace("\n", "").split(",")
    card_dict[card[0]] = int(card[1])
    card_list.append(card[0])
all_cards.close()


def voucher_generation():
    """ Creates Voucher text file at the end of the game. """
    voucher_file = open("voucher.txt", "w")
    print("\n-----------------------------------------------------------", file=voucher_file)
    print("Blackjack Voucher", end="", file=voucher_file)
    print(player1, file=voucher_file)
    print("-----------------------------------------------------------", file=voucher_file)


# REPEATING FUNCTIONALITY


def betting():
    """ Betting functionality which first checks the players token count and decides if they can
    play on or how much they can bet on the next round."""
    while True:
        if player1.token_count() == 0:
            print("\nSorry, you don't have any more tokens to keep playing, ending the game now.")
            time.sleep(2.0)
            print(player1)
            player1()
            voucher_generation()
            sys.exit()
        try:
            bet = int(input(f"\nYou have {player1.token_count()} tokens. Please place your bet:"))
            if bet > player1.token_count():
                print(f"You can only bet up to {player1.token_count()} tokens.")
                raise AttributeError
            elif bet == 0:
                print(f"You can must bet at least 1 token to play.")
                raise AttributeError
            else:
                return bet
        except ValueError:
            print("Error, enter a valid bet.")




def draw_card(whose_cards):
    """ Randomly draws a card from the card deck and removes it from being chosen again. """
    for i in range(1):
        x = random.choice(copy_of_card_list)
        whose_cards.append(x)
        copy_of_card_list.remove(x)


def print_player_cards(hand):
    """ Prints out the cards within the players hand. """
    temp_string = ""
    for i in hand:
        temp_string += i + ", "
    temp_string = temp_string[:len(temp_string) - 2]
    print(f"Players cards: {temp_string}")


def print_dealer_cards(hand):
    """ Prints out the cards within the dealers hand. """
    temp_string = ""
    for i in hand:
        temp_string += i + ", "
    temp_string = temp_string[:len(temp_string) - 2]
    print(f"Dealers cards: {temp_string}")


def hand_value(hand):
    """ Checks for the numerical value of a hand. """
    hand_total = 0
    for q in hand:
        hand_total += card_dict[q]
    if hand_total > 21:  # Accounts for ace value either being 11 or 1 (if it puts your hand over 21)
        for z in hand:
            if z == "Ace of Hearts":
                hand_total -= 10
            elif z == "Ace of Spades":
                hand_total -= 10
            elif z == "Ace of Diamonds":
                hand_total -= 10
            elif z == "Ace of Clubs":
                hand_total -= 10
    return hand_total


def amount_check_player():
    """ Specifically checks for the player's hand value. """
    player_amount = hand_value(players_cards)
    return player_amount


def amount_check_dealer():
    """ Specifically checks for the dealer's hand value. """
    dealer_amount = hand_value(dealers_cards)
    return dealer_amount


def player_h_or_s(value):
    """ Function which either notifies the player they have Blackjack/Bust, or if they have a hand value
    below 21, implements looping functionality that allows the player to hit or stand."""
    if value == 21:
        print("You have BlackJack!")
        time.sleep(1.5)
    elif value > 21:
        print("Bust!")
        time.sleep(1.5)
    else:
        while True:
            try:
                hit_or_stand = input("\n\nWill you hit (H) or stand (S)? Please type H or S: ").upper()
                if hit_or_stand == "H" or hit_or_stand == "S":
                    if hit_or_stand == "H":
                        draw_card(players_cards)
                        print_player_cards(players_cards)
                        value = hand_value(players_cards)
                        player_h_or_s(value)
                        break
                    if hit_or_stand == "S":
                        break
                else:
                    raise ValueError
            except ValueError:
                print("Error please type in a proper response.")


def dealer_h_or_s(value):
    """ Decides dealers actions based on traditional casino rules such as automatically standing when
    the dealer has 17 or more and hitting until they either have Blackjack, bust or meet that rule."""
    if value == 21:
        print_dealer_cards(dealers_cards)
    elif value > 21:
        print_dealer_cards(dealers_cards)
    else:
        if value >= 17:
            print_dealer_cards(dealers_cards)
        else:
            draw_card(dealers_cards)
            value = hand_value(dealers_cards)
            dealer_h_or_s(value)


def player_win():
    """ Player win commands which show the player winning and gaining the coins they bet. """
    print("Player wins!", end="")
    player1.token_win(player_bet)
    player1.add_win()


def dealer_win():
    """ Dealer win commands which have the player losing the coins they bet. """
    print("Dealer wins!", end="")
    player1.token_loss(player_bet)
    player1.add_loss()


def no_win():
    """ Notifies of a tie with no changes to the players tokens. """
    print("It's a tie. No one wins", end="")


def who_wins():
    """ Decides who wins based on comparing the hand values of the player and dealer. """
    time.sleep(1.5)
    print("\nAnd the", end=" ")
    if player_value == 21:
        if dealer_value == 21:
            no_win()
        else:
            player_win()
    elif player_value > 21:
        dealer_win()
    else:
        if dealer_value > 21:
            player_win()
        elif dealer_value == 21:
            dealer_win()
        elif player_value > dealer_value:
            player_win()
        elif player_value < dealer_value:
            dealer_win()
        else:
            no_win()
    print("\n-----------------------------------------------------------\n\n")  # Prints a divider to show end of turn


def play_check():
    """ Asks the player if they want to play again. If yes, another round will start, if no, the game ends. """
    while True:
        try:
            play_question = input("Do you want to play again (Y or N): ").capitalize().strip()
            if play_question == "Y" or play_question == "N":
                break
            else:
                raise ValueError
        except ValueError:
            print("Error, please enter either Y for yes OR N for no.\n")
    return play_question


# Main Game


if __name__ == "__main__":
    play_again = "Y"
    while play_again == "Y":

        player_bet = betting()
        player1.add_round()

        dealers_cards = []
        players_cards = []
        copy_of_card_list = copy.deepcopy(card_list)

        draw_card(dealers_cards)  # Draws the dealer's first card.
        draw_card(dealers_cards)  # Draws the dealer's second card.
        draw_card(players_cards)  # Draws the player's first card.
        draw_card(players_cards)  # Draws the player's second card.

        print(f"\nDealers cards: Face down, {dealers_cards[1]}")  # only reveals the dealer's second card
        print_player_cards(players_cards)

        player_value = amount_check_player()
        dealer_value = amount_check_dealer()

        player_h_or_s(player_value)
        print("\nTime to check the dealer's cards.")
        dealer_h_or_s(dealer_value)

        player_value = amount_check_player()
        dealer_value = amount_check_dealer()
        who_wins()

        play_again = play_check()

    if play_again == "N":
        print(player1)
        player1()
        voucher_generation()
        sys.exit()
