# what is the 10001st prime number
primes = [2]
i = 3  # Start checking from 3

while True:
    for prime in primes:
        if prime * prime > i:
            # i is a prime number
            primes.append(i)
            if len(primes) >= 10001:
                print("The 1001st prime number is:", primes[10000])
                exit()
            break
        if i % prime == 0:
            # i is not a prime number
            break
    else:
        # If the loop completes without breaking, i is a prime number
        primes.append(i)

    i += 2  # Increment by 2 to check only odd numbers (except 2, which is already in primes)
