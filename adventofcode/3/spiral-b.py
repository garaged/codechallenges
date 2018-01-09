import math
import sys

def spiral(width, max_num):
  matrix = [[None] * width for i in range(width)]
  N, S, W, E = (0,-1), (0, 1), (-1, 0), (1, 0)
  turn = { E: N, N: W, W: S, S: E }
  x, y = width // 2, width // 2 # (almost) mid point
  dx, dy = S # initial dir
  count = 1
  matrix[y][x] = count
  while True:
    new_dx, new_dy = turn[dx, dy]
    new_x, new_y = x + new_dx, y + new_dy
    if ( 0 <= new_x < width and 0 <= new_y < width and matrix[new_y][new_x] is None): # try turn
      x, y = new_x, new_y
      #print_mat(matrix)
      matrix[y][x] = sum_square(matrix, x, y, width, max_num)
      dx, dy = new_dx, new_dy
    else:                         # continue straight
      x, y = x + dx, y + dy
      if not ( 0 <= x < width and 0 <= y < width):
        return matrix # the end
      matrix[y][x] = sum_square(matrix, x, y, width, max_num)

def print_mat(m):
  for i in range(len(m)):
    print(m[i])

def sum_square(matrix, x, y, width, max_num):
  sum = 0
  y_1 = 0 if y - 1 < 0 else y - 1
  x_1 = 0 if x - 1 < 0 else x - 1
  y_2 = y + 1 if y + 2 >= width else y + 2
  x_2 = x + 1 if x + 2 >= width else x + 2
  for j in range(y_1, y+2):
    for i in range(x_1, x+2):
      try:
        #print("suma2", j,i, matrix[j][i])
        sum += matrix[j][i]
      except:
        #print("falla")
        pass
  if sum > max_num:
    print("mayor", x, y, sum, ">", max_num)
    sys.exit(0)
  return sum


num = 312051
#num = 25
width = math.ceil(math.sqrt(num))
spiral(width, num)
