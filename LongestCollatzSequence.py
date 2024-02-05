# Collatz sequence, which number under 1 mill produces the longest collatz chain
record = []
starting = 999999

for i in range(starting, 0, -1):
    chain = []
    number = i
    while i > 1:
        if i % 2 == 0:
            i = i // 2  # Use integer division
        else:
            i = 3 * i + 1
        chain.append(i)
    record.append([number, len(chain)])

# Sort and print the result
sortd = sorted(record, key=lambda x: x[1], reverse=True)
print(sortd[0])  # [837799, 524]
