import random

name = input("Who are you?\n> ")
print(f"Hello, {name}!")

print("Tossing a coin...")
results = {"Heads": 0, "Tails": 0}

for i in range(3):
    result = random.choice(["Heads", "Tails"])
    results[result] += 1
    print(f"Round {i + 1}: {result}")

print(f"Heads: {results['Heads']}, Tails: {results['Tails']}")

if results["Heads"] > results["Tails"]:
    print("You won!")
else:
    print("You lost!")

