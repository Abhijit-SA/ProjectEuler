from math import comb

grid = int(input("Enter grid size (e.g., 2x2): "))
# print(fact(2 * grid) // (fact(grid) * fact(grid)) # literally the same thing..
print(comb(2 * grid, grid))
