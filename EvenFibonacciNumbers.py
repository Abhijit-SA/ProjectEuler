# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
first = 1
second = 2
sum = 0
even_terms = 0

while second < 4000000:
    if second % 2 == 0:
        even_terms += second
    sum = first + second
    first = second
    second = sum

print(even_terms)  # output: 4613732
