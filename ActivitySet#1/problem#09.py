# Lists
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.strip()
    words=line.split()
for word in words : 
    if word not in lst:
        list.append(word)
print(sorted(lst))



