# Find the smallest possible number that is divisble by every number between 1 and 20
primes = [2, 3, 5, 7, 11, 13, 17, 19]
print(len(primes))
number = 20 * 2

while True:
    for i in range(2,20):
        if number % i != 0:
            break
    else:
        print(number)
        break

    number += 20  # Increment by the maximum divisor (20 in this case)
