import pandas as pd
data = pd.read_csv("spread.csv", header=None, sep="\t").T

sum = 0
for i in data:
  for j in range(len(data[i])):
    for k in range(j + 1, len(data[i])):
      if data[i][j] % data[i][k] == 0:
        sum = sum + data[i][j]/data[i][k]
      elif data[i][k] % data[i][j] == 0:
        sum = sum + data[i][k]/data[i][j]
print(sum)
