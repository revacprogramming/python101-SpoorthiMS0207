# Strings

text = "X-DSPAM-Confidence:    0.8475";
length = text.find(':')
number = float(text[length+1:])
print(number)
