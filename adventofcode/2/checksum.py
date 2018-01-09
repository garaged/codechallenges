import pandas as pd
data = pd.read_csv("spread.csv", header=None, sep="\t")
data2 = data.T
suma = 0
for i in data2:
  suma = suma + max(data2[i])- min(data2[i])
print (suma)
