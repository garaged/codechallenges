import sys
import re
#f = open("tree.txt", "r") # this is my data
f = open("test.txt", "r")
l = f.readlines()

# Warning really ugly code ahead ! 

# parsing regex 
p1 = re.compile('(\w+)\s+\((\d+)\)\s+->\s+(.*$)')
              # 'fwft (72) -> ktlj, cntj, xhth'
p2 = re.compile('(\w+)\s+\((\d+)\)')
              # 'fwft (72) -> ktlj, cntj, xhth'

# This will create the tree from data file in the form of a dictionary
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
  weight[row[0]] = int(row[1])
for i in parents.keys():
  is_child[i] = False
  for j in parents.keys():
    if type(parents[j]) is list:
      if i in parents[j]:
        is_child[i] = True

#print(parents)

def weight_sum(parent):
  """Return the cummulative sum of weights for a branch (including parent)"""
  sum = 0
  if type(parents[parent]) is list:
    for i in parents[parent]:
      sum += weight[i]
      if type(parents[i]) is list:
        for j in parents[i]:
          if is_child[j]:
            sum +=  weight_sum(j)
  return sum + weight[parent]

def print_sum_r(n, parent): 
  """travels tree returning cummulative sum for every parent (has childs)
  n -> indent level (for printin)
  parent -> first parent for this run"""
  if type(parents[parent]) is list:
    #print("list ", parents[parent])
    pts = 0
    for i in parents[parent]:
      tot = weight_sum(i)
      n += 1
      print_sum_r(n, i)
      n -= 1
      print("{} {}->{} tot = {} ".format(" "*n, parent, i, tot))
  return True

n = 0 # indent level
#first = 'bpvhwhh' # this is my data
first = 'tknk'
print(first, weight_sum(first))
print_sum_r(n, first)
