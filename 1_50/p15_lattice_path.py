''' No ow Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.'''
import math
n=int(input()) #size of grid
total_path=2*n
print(int(math.factorial(total_path)/(math.factorial(n)**2)))
