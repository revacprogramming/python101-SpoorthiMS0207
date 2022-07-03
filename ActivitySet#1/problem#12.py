# Regular Expressions
# https://www.py4e.com/lessons/regex
import re

hand = open('a.txt')
all_lines = hand.read() 
all_str_nums_as_one_line = re.findall('[0-9]+',all_lines)
hand.close()
tot = 0
for str_num in all_str_nums_as_one_line:
    tot += int(str_num)

print('Overall sum is:',tot) 

