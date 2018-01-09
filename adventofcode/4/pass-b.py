def check_pass(pp):
  words=pp
  for i in range(len(words)):
    for j in range(i+1, len(words)):
      if ( words[i] == words[j] or is_anagram(words[i], words[j]) ):
        print(pp, "no pasa")
        return False
  print(pp, "si pasa")
  return True

def is_anagram(w1, w2):
  print("is", w1, w2)
  list_str1 = list(w1)
  list_str2 = list(w2)
  list_str1.sort()
  list_str2.sort()
  return ( list_str1 == list_str2)


import csv
f = open("passphrases", "r")
p = csv.reader(f, delimiter=" ")
#print(p)
cnt = 0
for i in p:
  print("check ", i, type(i))
  if check_pass(i):
    cnt += 1
print("total:", cnt)
