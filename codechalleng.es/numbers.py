from collections import Iterable
def sum_numbers(numbers=None):
  sum_n = 0
  try:
    is_iter = isinstance(numbers, Iterable) 
  except:
    is_iter = False
  if is_iter:
    for i in numbers:
      sum_n += i
  else:
    for i in range(1,101):
      sum_n += i
  return sum_n
