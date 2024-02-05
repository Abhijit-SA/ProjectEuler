def number_to_words(num):
    # Define the words for each digit
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    teens = [
        "",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    tens = [
        "",
        "ten",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]

    # Define the words for each magnitude
    thousands = ["", "thousand", "million", "billion", "trillion"]

    def convert_below_thousand(n):
        if n == 0:
            return ""
        elif n <= 10:
            return ones[n]
        elif n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
        else:
            return (
                ones[n // 100]
                + " hundred"
                + (" and " + convert_below_thousand(n % 100) if n % 100 != 0 else "")
            )

    if num == 0:
        return "zero"

    result = ""
    magnitude = 0

    while num > 0:
        triplet = num % 1000
        if triplet > 0:
            result = (
                convert_below_thousand(triplet)
                + " " # could remove these because we are using strip/replacing this anyway
                + thousands[magnitude]
                + " " # but i will leave it here in case i need this cool function later.
                + result
            )
        magnitude += 1
        num //= 1000

    return result.strip()


if __name__ == "__main__":
    count = 0
    for number in range(1, 1001):
        print(number_to_words(number).replace(" ", "").replace("-", ""))
        count += len(number_to_words(number).replace(" ", "").replace("-", ""))
    print(count)
