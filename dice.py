import random

print("🎲 Welcome to the Dice Roller Simulator!")

# Get user inputs
num_dice = int(input("How many dice do you want to roll? "))
num_sides = int(input("How many sides does each die have? "))

# Roll the dice
rolls = []
for _ in range(num_dice):
    roll = random.randint(1, num_sides)
    rolls.append(roll)

# Show the results
print(f"\nYou rolled: {rolls}")
print(f"Total: {sum(rolls)}")
print("hello world")
