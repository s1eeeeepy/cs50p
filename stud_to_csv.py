import csv
import sys


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if sys.argv[1][-4:] != ".csv" or sys.argv[2][-4:] != ".csv":
    sys.exit("Not a CSV file")
try:
    students = []
    names = []
    with open(sys.argv[1]) as b:
        reader = csv.DictReader(b)
        for row in reader:
            students.append({"name": row["name"], "house": row["house"]})
        for student in students:
            names.append(
                {
                    "first": student["name"].split(", ")[1],
                    "last": student["name"].split(", ")[0],
                }
            )

    with open(sys.argv[2], "a") as a:
        writer = csv.DictWriter(a, fieldnames=["name", "house"])
        idx = 0
        for s in students:
            name = f"{names[idx]['first']}, {names[idx]['last']}"
            house = students[idx]["house"]
            writer.writerow({"name": name, "house": house})
            idx += 1


except FileNotFoundError:
    sys.exit("File does not exist")
