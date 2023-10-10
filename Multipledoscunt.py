https://replit.com/join/spcxypaovy-elianguerrero1 
### Multiple discount calculator:+

product = float(input("Put the price of the product: "))
category = input("Put the category (A, B, C): ")
units = int(input("Number of units purchased: "))

discount = 0
additional_discount = 0
G = product * units
if category == "A": 
  F = (G)*.10
  discount = G - F

elif category == "B": 
  F = (G)*.05
  discount = G - F

elif category == "C":
  F = (G)*.02
  discount = G - F

if units >= 10:
  R = (discount)*.05  
  additional_discount = discount - R
print("This is your final price", additional_discount)
if units < 10:
  print("This is your final price", discount)
