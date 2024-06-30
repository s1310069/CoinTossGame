import random

print("Tossing a coin...")
result = {"Heads": 0, "Tails": 0}

for i in range(3):
    result = random.choice(["Heads", "Tails"])
    result[result] += 1
    print(f"Round {i + 1}: {result}")

print(f"Heads: {results['Heads']}, Tails: {results['Tails']}")
