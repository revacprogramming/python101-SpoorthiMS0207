# Dictionaries

filename = "dataset/mbox-short.txt"
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
text = open(name)
max=dict()
for line in text :
  line.rstrip()
  if not line.startswith ("from"):
    continue :
    word=line.split()






