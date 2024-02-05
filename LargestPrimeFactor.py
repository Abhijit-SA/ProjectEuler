# What is the largest prime factor of the number 600851475143?
def largest_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


number = 600851475143
result = largest_factor(number)
print(f"The largest factor of {number} is: {result}")
