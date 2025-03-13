# import random
# from collections import Counter

# def rollDice(num_dice):
#     return [random.randint(1, 6) for _ in range(num_dice)]

# def countOutcomes(dice):
#     return Counter(dice)

# def selectOutcome(outcomes):
#     valid_outcomes = {outcome: count for outcome, count in outcomes.items() if count > 1}
#     if not valid_outcomes:
#         return None
#     # print(f"Valid outcomes to select from: {valid_outcomes}")
#     while True:
#         try:
#             selection = int(input("Select an outcome that occurred more than once: "))
#             if selection in valid_outcomes:
#                 return selection
#             else:
#                 print("Invalid selection. Please select an outcome that occurred more than once.")
#         except ValueError:
#             print("Invalid input. Please enter a number.")

# def multiplesStay():
#     num_dice = 10
#     player = 1

#     while num_dice > 0:
#         print(f"Player {player}'s turn")
#         dice = rollDice(num_dice)
#         print(f"Rolled dice: {dice}")

#         outcomes = countOutcomes(dice)
#         print(f"Dice outcomes: {outcomes}")

#         selected_outcome = selectOutcome(outcomes)
#         if selected_outcome is None:
#             print("No valid outcomes to select. All dice will be rerolled.")
#         else:
#             num_dice -= outcomes[selected_outcome]
#             print(f"Player {player} selected outcome {selected_outcome}. {outcomes[selected_outcome]} dice removed.")
        
#         print(f"Remaining dice: {num_dice}")
#         player = 2 if player == 1 else 1

#     print("Game over! No more dice to roll.")

# multiplesStay()

import random
from collections import Counter

def rollDice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]

def countOutcomes(dice):
    return Counter(dice)

def selectOutcome(outcomes):
    valid_outcomes = {outcome: count for outcome, count in outcomes.items() if count > 1}
    if not valid_outcomes:
        return None
    while True:
        try:
            selection = int(input("Select an outcome: "))
            if selection in valid_outcomes:
                return selection
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input.")

def multiplesStay():
    num_dice = 10
    player = 1

    while num_dice > 0:
        print(f"Player {player}'s turn")
        dice = rollDice(num_dice)
        print(f"Rolled: {dice}")

        outcomes = countOutcomes(dice)
        print(f"Outcomes: {outcomes}")

        selected_outcome = selectOutcome(outcomes)
        if selected_outcome is None:
            print(f"No valid outcomes. Player {player} loses!")
            break
        else:
            num_dice -= outcomes[selected_outcome]
            print(f"Player {player} selected outcome {selected_outcome}. {outcomes[selected_outcome]} dice removed.")
        
        print(f"Remaining dice: {num_dice}")

        if num_dice == 0:
            print(f"All dice are removed. Player {player} wins!")
            
        player = 2 if player == 1 else 1 # Switch player

    print("Game over!")

multiplesStay()