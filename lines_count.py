import sys


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if sys.argv[-1][-3:] != ".py":
    sys.exit("Not a Python file")
try:
    with open(sys.argv[-1], "r") as f:
        lines = []
        for line in f:
            lines.append(line.strip())

    print(lines)
except FileNotFoundError:
    print("File does not exist")


amount = 0
for line in lines:
    try:
        if line[0] != "#" and line != "" and "'''" not in line and '"""' not in line:
            amount += 1
    except IndexError:
        pass

print(amount)
