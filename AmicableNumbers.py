def sum_of_divisors(n):
    divisors_sum = 1  # Include 1 as a divisor
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum


def find_amicable_numbers(limit):
    amicable_numbers = set()

    for a in range(2, limit):
        b = sum_of_divisors(a)
        if b != a and sum_of_divisors(b) == a:
            amicable_numbers.add(a)
            amicable_numbers.add(b)
    return amicable_numbers


print(sum(find_amicable_numbers(10000)))
