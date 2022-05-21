# Files
fname = input("mbox-short.txt")
fh = open(fname)
count = 0
average = 0
for line in fh:
        if not line.startswith("X-DSPAM-Confidence:"):
        continue
        average = average + float(line[20:-1].strip())
        count = count + 1
print("Average spam confidence:",(average/count))

