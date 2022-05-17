# Files

largest = 0
smallest = 0
c=1
while True:
    num = input("Enter a number: ")
    
    if num == "done":
        break

    try:
      num = int(num)

    except:
      print('Invalid input')
    if c==1:
        largest=num
        smallest=num  
    c=c+1 
    if largest < num :
        largest = num
    elif smallest > num :
        smallest = num
        
  
      

print("Maximum is", largest)
print("Minimum is", smallest)

