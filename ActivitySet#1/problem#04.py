# Conditional Execution

hrs = input("Enter Hours:")
h = float(hrs)
rate=input("Enter Rate:")
rate=float(rate)
if h<=40 :
    pay = h*rate
else:
    pay= 40*rate + 1.5*rate*(h-40)
print(pay)
    