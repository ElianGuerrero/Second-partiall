
https://replit.com/join/rrwmyosobr-elianguerrero1



print("What is the ambient temperature?")
temperature = int(input())
if temperature > 25:
  print("Bring it inside the house and turn on the fan.")
elif temperature < 20:
  print("Bring it inside the house.")
elif 25 > temperature > 20:
  print("Good conditions")
else:
  print("Put a valid answer please")


print("What day is it? put it all in lowercase please.")
day = input()
if day == "tuesday" or day == "thursday" or day == "saturday":
  print("Water Ruby please")
else:
  print("Do not water ruby")

  

print("What is the number of humidity?")
humidity = int(input())
if humidity < 20:
  print("You should water it")

elif humidity > 22 and day == "monday" or day == "wednesday" or day == "friday" or day == "sunday":
  print("Its necessary to water Ruby")
