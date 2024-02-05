# Find sum of all multiples of 3 and 5
sum = 0
for i in range(0,1000):
    if i % 3 == 0:
        sum += i
    elif i % 5 == 0:
        sum += i
print(sum) # output: 266168