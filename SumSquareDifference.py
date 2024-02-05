# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
sumofsqaure = 0
squareofsum = 0
for i in range(0, 101):
    sumofsqaure += i * i
    squareofsum += i
print(abs(sumofsqaure - squareofsum * squareofsum))
