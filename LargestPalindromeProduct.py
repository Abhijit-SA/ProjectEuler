# find the largest palindrome of the product of two 3-digit numbers

largest = 0

for i in range(100, 999):
    for j in range(100, 999):
        if str(i * j) == (str(i * j)[::-1]):
            print(i * j)
            if largest < i * j:
                largest = i * j
print(largest)  # output: 906609
