# what is the sum of the digits in 2**1000
val = 2**1000
sum = 0
while val > 0:
    sum = sum + val % 10
    val = val // 10
print(sum)