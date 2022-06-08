# Strings

text = "X-DSPAM-Confidence:    0.8475";
length = text.find(':')
num = float(text[length+1: ])
print(num)
