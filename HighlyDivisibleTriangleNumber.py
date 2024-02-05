# What is the value of the first triangle number to have over five hundred factors?


def find_factors(number):
    factors = []
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            factors.append(i)
            if i != number // i:  # Avoid duplicates for perfect squares
                factors.append(number // i)
    return factors


n = 0
while True:
    triangle = n * (n + 1) // 2
    factors = find_factors(triangle)
    if len(factors) > 500:
        print(triangle)
        exit()
    n += 1
