# sum of primes below 2 mill
import time

start_time = time.time()
primes = [2]
i = 3  # Start checking from 3

while i < 2000000:
    for prime in primes:
        if prime * prime > i:
            # i is a prime number
            primes.append(i)
            break
        if i % prime == 0:
            # i is not a prime number
            break
    else:
        # If the loop completes without breaking, i is a prime number
        primes.append(i)
    i += 2  # Increment by 2 to check only odd numbers (except 2, which is already in primes)

print(sum(primes))
end_time = time.time()
execution_time = end_time - start_time
print(execution_time)