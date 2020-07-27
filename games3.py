import sys
import random

money = 100  # default money value
username = "user"  # default username


# functions

def initialize():
    global username
    username = input("Enter Username: ")
    print("Hello, " + username + ".")
    return money_response()


def money_response():
    global money
    try:
        money = int(input("How much money would you like to start with?\n$"))
    except ValueError:
        print("Please enter a number.")
        return money_response()
    if money == 69:
        print("Haha, nice!")
        print(current_balance())
        return game_choice()
    elif money > 1000:
        print("$1000 is the maximum starting amount!")
        print("Please enter an amount of $1000 or less.")
        return money_response()
    elif money <= 0:
        print("$1 is the minimum starting amount!")
        print("Please enter an amount of $1 or greater.")
        return money_response()
    else:
        print("$" + str(money) + " has been added to your balance.")
        print(current_balance())
        return game_choice()


def current_balance():
    balance = ("Current Balance: $" + str(money))
    if money == 69:
        return balance + " lol"
    else:
        return balance


def game_choice():
    prompt = input("Which game would you like to play? \n'1' for Coin Toss \n'2' for Cho Han \n\
'3' for Pick A Card \n'4' for Roulette \n")
    if prompt == "1":
        return coin_toss()
    elif prompt == "2":
        return cho_han()
    elif prompt == "3":
        print("Sorry, that game has not been coded yet!")
        return game_choice()
    elif prompt == "4":
        print("Sorry, that game has not been coded yet!")
        return game_choice()
    else:
        print("Please make a valid choice!")
        return game_choice()


def play_again(game):
    if win_condition() == "win":
        return victory()
    elif win_condition() == "lose":
        return game_over()
    elif win_condition() == "null":
        replay = y_or_no("play again?")
        if replay:
            if game == 1:
                return coin_toss()
            elif game == 2:
                return cho_han()
            elif game == 3:
                return game_choice()
            elif game == 4:
                return game_choice()
            else:
                return play_again(game)
        elif not replay:
            diff_game = y_or_no("choose a different game?")
            if diff_game:
                return game_choice()
            else:
                quit = y_or_no("quit?")
                if quit:
                    sys.exit("Thank you for playing!")
                else:
                    return play_again(game)


def place_bet():
    global money
    try:
        bet_amt = int(input("How much would you like to bet? (Balance: $" + str(money) + ") \n$"))
    except ValueError:
        print("Please enter a number.")
        return place_bet()
    if bet_amt > money:
        print("You can't bet more than your current balance!")
        return place_bet()
    elif bet_amt == money:
        money += -bet_amt
        print("All In! Winnings will be doubled!")
        print(current_balance())
        return bet_amt * 2
    elif money >= bet_amt > 0:
        money += -bet_amt
        print("You bet $" + str(bet_amt) + "!")
        print(current_balance())
        return bet_amt
    else:
        print("Please make a valid bet.")
        return place_bet()


def y_or_no(question):
    choice = input("\nWould you like to " + question + " Y/N? ")
    if choice == "Y" or choice == "y":
        return True
    elif choice == "N" or choice == "n":
        return False
    else:
        print("Please type \"Y\" or \"N\".")
        return y_or_no(question)


def win_condition():
    if money >= 5000:
        return "win"
    elif money <= 0:
        return "lose"
    else:
        return "null"


def game_over():
    print("Game Over!")
    y_or_n = input("Would you like to start over, Y or N? ")
    if y_or_n == "Y" or y_or_n == "y":
        return initialize()
    elif y_or_n == "N" or y_or_n == "n":
        sys.exit("Thank you for playing!")
    else:
        print("You must enter Y or N.")
        return game_over()


def victory():
    print("Congratulations! You Win! Final Balance: $" + str(money))
    y_or_n = input("Would you like to start over, Y or N? ")
    if y_or_n == "Y" or y_or_n == "y":
        return money_response()
    elif y_or_n == "N" or y_or_n == "n":
        sys.exit("Thank you for playing!")
    else:
        print("You must enter Y or N.")
        return victory()


# game functions

def coin_toss():
    global money
    num = random.randint(1, 2)
    print("You are playing coin toss.")

    def heads_or_tails():
        h_or_t = input("Do you choose heads or tails? Type H or T. ")
        if h_or_t == "H" or h_or_t == "h":
            return "heads"
        elif h_or_t == "T" or h_or_t == "t":
            return "tails"
        else:
            print("Please enter either \"H\" or \"T\".")
            return heads_or_tails()

    choice = heads_or_tails()
    bet = place_bet()
    print("\nCoin flipped!")
    if username == "cheatcodes":
        money += (bet * 2)
        print("Cheater! You Won $" + str(bet * 2) + "! " + current_balance())
        return play_again(1)
    elif choice == "heads" and num == 1:  # heads and win
        money += (bet * 2)
        print("It's Heads! You Won $" + str(bet * 2) + "! " + current_balance())
        return play_again(1)
    elif choice == "tails" and num == 2:  # tails and win
        money += (bet * 2)
        print("It's Tails! You Won $" + str(bet * 2) + "! " + current_balance())
        return play_again(1)
    elif choice == "heads" and num == 2:  # heads and lose
        print("It's Tails... you lost this round. " + current_balance())
        return play_again(1)
    elif choice == "tails" and num == 1:  # tails and lose
        print("It's Heads... you lost this round. " + current_balance())
        return play_again(1)


def cho_han():
    global money
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("You are playing Cho Han.")

    def odd_or_even():
        o_or_e = input("Do you choose odd or even? Type O or E.")
        if o_or_e == "O" or o_or_e == "o":
            return "odd"
        if o_or_e == "E" or o_or_e == "e":
            return "even"
        else:
            print("Please enter either \"O\" or \"E\".")
            return odd_or_even()

    def dice_results(d1, d2):
        total = d1 + d2
        odd_even_result = total % 2
        print("\nThe first dice rolled a " + str(d1) + ".")
        print("The second dice rolled a " + str(d2) + ".")
        if odd_even_result == 0:
            print("\nTotal of both dice is " + str(total) + ". Even!")
            return "even"
        else:
            print("\nTotal of both dice is " + str(total) + ". Odd!")
            return "odd"

    choice = odd_or_even()
    bet = place_bet()
    result = dice_results(dice1, dice2)

    if choice == result:
        money += bet * 2
        print("You chose " + choice + ", so you win $" + str(bet * 2) + "!")
        current_balance()
        return play_again(2)
    else:
        print("You chose " + choice + "... You lost $" + str(bet) + ".")
        current_balance()
        return play_again(2)


initialize()
