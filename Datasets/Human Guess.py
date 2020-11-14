from csv import DictReader
from random import choice, randint
file = "LiarLiarDataset_Full.csv"
data_texts,data_labels=[],[]
with open(file, encoding='utf-8') as f:
    for row in  DictReader(f):
        data_texts.append(row["Text"])
        data_labels.append(row["Label"])

both=[data_texts,data_labels]

for i in range(10):
    x=randint(0,len(data_labels))
    print(both[0][x])
    input("Guess the category True, mostly-true, half-true, barely-true, flase, or Pants-fire")
    print(both[1][x])
    input("Did you get it right?----------------------")
