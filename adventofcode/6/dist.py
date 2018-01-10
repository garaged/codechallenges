import numpy as np
import sys

f = open("puzzle.txt")
l = f.readline()
l = np.array(list(map(int, l.split("\t"))))
print(l)
steps = 0
hist = {}
hist_steps = {}
hist[tuple(l)] = 1
while True:
  pos = l.argmax()
  dist = l[pos]
  l[pos] = 0
  while dist > 0:
    pos = pos + 1
    if (pos > len(l)-1):
      pos = 0
    l[pos] += 1
    dist -= 1
    #print(l, pos, dist)
  steps += 1
  if tuple(l) in hist:
    hist[tuple(l)] += 1
  else:
    hist[tuple(l)] = 1
    hist_steps[tuple(l)] = steps
  print(l)

  if (hist[tuple(l)] > 1):
    print("se repite: ", l, steps)
    print("pasos: ", hist_steps[tuple(l)], steps, hist_steps[tuple(l)] - steps )
    sys.exit(0)
