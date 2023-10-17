https://replit.com/join/jboctvomja-elianguerrero1 

print("What is the ammount of your shopping?")
shopping = float(input())
print("Do you have a membership card?")
card = input()
shopping2 = int(shopping * .10)
if shopping >= 100:
  print(shopping - shopping2)  
  print("You have a 10% discount")
elif shopping < 100:
    print("You do not have a 10% discount")
shopping4 = int(shopping - shopping2)
shopping3 = int(shopping4 * .06) 

if card == "yes":
  print("You have a 5% discount")
  print("Your total is", int(shopping4 - shopping3))
elif card == "no":
  print("Your total is:", shopping - shopping2)
