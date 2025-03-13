# import random

# def rollDice():
#     return random.randint(1,6)

# def pig():
#     player1Score = 0
#     player2Score = 0
#     turn = 1

#     while True:
#         print(f"Player {turn}'s turn")
#         turnScore = 0
#         while True:
#             roll = rollDice()
#             print(f"Rolled: {roll}")
#             if roll == 1:
#                 print("Rolled a 1! Turn over.")
#                 turnScore = 0
#                 break
#             else:
#                 turnScore += roll
#                 print(f"Turn score: {turnScore}")
#                 if player1Score + turnScore >= 100 or player2Score + turnScore >= 100:
#                     break
#                 if turnScore >= 17:
#                     break
#                 # choice = input("Roll again? (y/n): ")
#                 # if choice.lower() != 'y':
#                 #     break

#         if turn == 1:
#             player1Score += turnScore
#             print(f"Player 1 score: {player1Score}")
#             if player1Score >= 100:
#                 print("Player 1 wins!")
#                 break
#             turn = 2
#         else:
#             player2Score += turnScore
#             print(f"Player 2 score: {player2Score}")
#             if player2Score >= 100:
#                 print("Player 2 wins!")
#                 break
#             turn = 1
#     print("Game over!")

# pig()

import random

def rollDice():
    return random.randint(1, 6)

def pig():
    player = 0
    game_over = False

    while not game_over:
        print(f"{player}'s turn")
        turnScore = 0
        rolling = True

        while rolling:
            roll = rollDice()
            print(f"Rolled: {roll}")
            if roll == 1:
                print("Rolled a 1! Turn over.")
                turnScore = 0
                rolling = False
            else:
                turnScore += roll
                print(f"Turn score: {turnScore}")
                if {player} + turnScore >= 100:
                    rolling = False
                elif turnScore >= 17:
                    rolling = False

        if turn == 1:
            player += turnScore
            print(f"Player 1 score: {player}")
            if {player} >= 100:
                print("{player} wins!")
                game_over = True
            else:
                turn = 2
        # else:
        #     player2Score += turnScore
        #     print(f"Player 2 score: {player2Score}")
        #     if player2Score >= 100:
        #         print("Player 2 wins!")
        #         game_over = True
        #     else:
        #         turn = 1

        player = 1 if player == 2 else 2

    print("Game over!")

# pig()

import random
import time

def rollDice():
    return random.randint(1,6)

def pig():
    player1Score = 0
    player2Score = 0
    turn = 1

    while True:
        print(f"Player {turn}'s turn")
        turnScore = 0
        while True:
            roll = rollDice()
            print(f"Rolled: {roll}")
            if roll == 1:
                print("Rolled a 1! Turn over.")
                turnScore = 0  # Reset turnScore to zero
                break
            else:
                turnScore += roll
                print(f"Turn score: {turnScore}")
                if player1Score + turnScore >= 100 or player2Score + turnScore >= 100:
                    break
                if turnScore >= 20:
                    break

        if turn == 1:
            player1Score += turnScore
            print(f"Player 1 score: {player1Score}")
            if player1Score >= 100:
                print("Player 1 wins!")
                break
            turn = 2
        else:
            player2Score += turnScore
            print(f"Player 2 score: {player2Score}")
            if player2Score >= 100:
                print("Player 2 wins!")
                break
            turn = 1
        
        # Add a delay to simulate time between rounds
        time.sleep(1)
    print("Game over!")

pig()