import math

def spiral(width):
  matrix = [[None] * width for i in range(width)]
  N, S, W, E = (0,-1), (0, 1), (-1, 0), (1, 0)
  turn = { E: N, N: W, W: S, S: E }
  x, y = width // 2, width // 2 # (almost) mid point
  dx, dy = E # initial dir

  count = 0
  while True:
    count += 1
    matrix[y][x] = count
    new_dx, new_dy = turn[dx, dy]
    new_x, new_y = x + new_dx, y + new_dy
    if ( 0 <= new_x < width and 0 <= new_y < width and matrix[new_y][new_x] is None):
      x, y = new_x, new_y
      dx, dy = new_dx, new_dy
    else:
      x, y = x + dx, y + dy
      if not ( 0 <= x < width and 0 <= y < width):
        return matrix # the end

num = 312051
width = math.ceil(math.sqrt(num))
import numpy as np
mat = np.array(spiral(width))
x, y = width // 2, width // 2
loc_y, loc_x = np.where(mat == num)
print(loc_x, loc_y)
print(mat[loc_y[0]][loc_x[0]])
d = abs(loc_x[0] - x) + abs(loc_y[0] - y)
print(d)


