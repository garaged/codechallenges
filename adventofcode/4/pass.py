def check_pass(pp):
  words = pp.split()
  for i in range(len(words)):
    for j in range(i+1, len(words)):
      if words[i] == words[j]:
        print(pp, "no pasa")
        return False
  print(pp, "si pasa")
  return True

p = ["aa bb cc dd ee", "aa bb cc dd aa", "aa bb cc dd aaa"]
f = open("passphrases", "r")
p = f.readlines()
cnt = 0
for i in p:
  if check_pass(i):
    cnt += 1
print("total:", cnt)
