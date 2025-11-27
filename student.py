import sys


scores = [10, 20, 30, 40, 50]


if len(sys.argv) <= 1:
    print("No scores provided. Using default values:", scores)
else:
    scores = [int(num) for num in sys.argv[1:]]

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print(f"Sum of scores = {total}")
print(f"Average score = {average:.2f}")
print(f"Maximum score = {maximum}")
print(f"Minimum score = {minimum}")
