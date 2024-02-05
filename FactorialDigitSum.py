from math import factorial as fact

val = fact(100)
sumOfDigits = 0
while val > 0:
    sumOfDigits = sumOfDigits + val % 10
    val = val // 10
print(sumOfDigits)
