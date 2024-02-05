from pathlib import Path

alphabets = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
names = sorted([name.strip('"') for name in Path("names.txt").read_text().split(",")])
totalSum = 0


if __name__ == "__main__":
    for name in names:
        sumOfAlphabets = 0
        while len(name) > 0:
            sumOfAlphabets += int(alphabets.index(name[0].lower()) + 1)
            name = name[1:]
        totalSum += sumOfAlphabets * (names.index(name) + 1)

    print(totalSum)
