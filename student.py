import sys
if len(sys.argv) < 2:
    print("Usage: python scores.py <scores>")
    sys.exit(1)

scores = list(map(int, sys.argv[1].split()))

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
