# import random

# def rollDice():
#     die1 = random.randint(1, 6)
#     die2 = random.randint(1, 6)
#     die3 = random.randint(1, 6)
#     die4 = random.randint(1, 6)
#     die5 = random.randint(1, 6)
#     return die1 + die2 + die3 + die4 + die5

# def rolltheBones():
#     playerScore = 0
#     playing = True

#     while playing:
#         guess = int(input("Enter your guess between 5 and 30: "))
#         if guess < 5 or guess > 30:
#             print("Invalid guess. Please enter a number between 5 and 30.")
#             continue

#         total = rollDice()
#         print(f"Rolled: {total}")

#         if total < guess:
#             points = 5 - guess
#             playerScore += points
#             print(f"Total is less than guess. You lose {points} points.")
#         elif total > guess:
#             points = guess - 5
#             playerScore += points
#             print(f"Total is more than guess. You gain {abs(points)} points.") # absolute value to ensure positive points
#         else:
#             playerScore += 50
#             print("Exact guess! You gain 50 points.") # this is the bonus for a perfect guess

#         print(f"Current score: {playerScore}")

#         while True:
#             choice = input("Do you want to play again? (y/n): ") # this ensures that the input is either y or n 
#             if choice.lower() in ['y', 'n']:
#                 break
#             print("Invalid input. Please enter 'y' or 'n'.")
        
#         if choice == 'n':
#             playing = False

#     print(f"Final score: {playerScore}")
#     print("Game over!")

# rolltheBones()

import random

def rollDice():
    dice = [random.randint(1, 6) for _ in range(5)]
    return sum(dice)

def rolltheBones():
    playerScore = 0
    totalTurns = 0
    playing = True

    while playing:
        guess = int(input("Enter your guess between 5 and 30: "))
        if guess < 5 or guess > 30:
            print("Invalid guess. Please enter a number between 5 and 30.")
            continue

        total = rollDice()
        print(f"Rolled: {total}")

        if total < guess:
            points = 5 - guess
            playerScore += points
            print(f"Total is less than guess. You lose {points} points.")
        elif total > guess:
            points = guess - 5
            playerScore += points
            print(f"Total is more than guess. You gain {abs(points)} points.")
        else:
            playerScore += 50
            print("Exact guess! You gain 50 points.")

        print(f"Current score: {playerScore}")
        totalTurns += 1

        while True:
            choice = input("Do you want to play again? (y/n): ")
            if choice.lower() in ['y', 'n']:
                break
            print("Invalid input. Please enter 'y' or 'n'.")

        if choice == 'n':
            playing = False

    if totalTurns > 0:
        averagePoints = playerScore / totalTurns
        print(f"Average points per turn: {averagePoints:.2f}")
    print(f"Final score: {playerScore}")
    print("Game over!")

rolltheBones()