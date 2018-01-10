import sys
import re
f = open("tree.txt", "r")
l = f.readlines()

p1 = re.compile('(\w+)\s+\((\d+)\)\s+->\s+(.*$)')
              # 'fwft (72) -> ktlj, cntj, xhth'
p2 = re.compile('(\w+)\s+\((\d+)\)')
              # 'fwft (72) -> ktlj, cntj, xhth'
parents = {}
weight= {}
is_child = {}
for i in l:
  m = p1.match(i)
  if m is None:
    m = p2.match(i)
  row = m.groups()
  if len(row) == 2: # has no childs
    parents[row[0]] = None
  elif len(row) == 3: # has childs
    parents[row[0]] = row[2].split(", ")
  weight[row[0]] = row[1]
for i in parents.keys():
  is_child[i] = False
  for j in parents.keys():
    if type(parents[j]) is list:
      if i in parents[j]:
        is_child[i] = True
print(is_child)
print(weight)
