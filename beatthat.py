# import random

# def rollDice():
#     die1 = random.randint(1,6) 
#     die2 = random.randint(1,6)
#     return max(die1, die2) * 10 + min(die1, die2)

# def beatThat():
#     player1Score = 0
#     player2Score = 0
#     turn = 1

#     while True:
#         print(f"Player {turn}'s turn")
#         roll = rollDice()
#         print(f"Rolled: {roll}")
#         if turn == 1:
#             player1Score += roll
#             print(f"Player 1 score: {player1Score}")
#             if player1Score >= 100:
#                 print("Player 1 wins!")
#                 break
#             turn = 2
#         else:
#             player2Score += roll
#             print(f"Player 2 score: {player2Score}")
#             if player2Score >= 100:
#                 print("Player 2 wins!")
#                 break
#             turn = 1
#     print("Game over!")

# beatThat()

import random

def rollDice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return max(die1, die2) * 10 + min(die1, die2)

def beatThat():
    player1Score = 0
    player2Score = 0
    game_over = False

    while not game_over:
        print("Player 1's turn")
        player1Roll = rollDice()
        print(f"Rolled: {player1Roll}")

        print("Player 2's turn")
        player2Roll = rollDice()
        print(f"Rolled: {player2Roll}")

        if player1Roll > player2Roll:
            player1Score += player1Roll
            print(f"Player 1: {player1Score} points")
        elif player2Roll > player1Roll:
            player2Score += player2Roll
            print(f"Player 2: {player2Score} points")
        else:
            print("It's a tie! No points awarded.")

        if player1Score >= 100:
            print("Player 1 wins the game!")
            game_over = True # check if player 1 has reached 100 points
        elif player2Score >= 100:
            print("Player 2 wins the game!")
            game_over = True # check if player 2 has reached 100 points

    print("Game over!")

beatThat()