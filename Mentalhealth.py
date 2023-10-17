https://replit.com/join/ezwxvwozyn-elianguerrero1

print("Hi, today we are going to make a quizz for your mental health")
print("Answer the following questions with a yes or a no")

print("Do you have a balanced diet?")
diet = input()

print("Do you do any kind of physical activity?")
exercise = input()

print("Do you do meditation or yoga?")
meditation = input()

print("Are you a social person?")
social = input()

print("Do you sleep from 7 to 9 hours a day?")
sleep = input()

print("Do you go out with friends?")
friends = input()

print("Do you like to spend time outside?")
outside = input()

if sleep == "yes" and exercise == "yes" and social == "yes" and diet == "yes" and meditation == "yes" and outside == "yes" and friends == "yes":
  print("You have a good menta health, keep going")
else:
  if sleep == "no":
    print("You should sleep more in order to have a healthy mind and body.")
  if exercise == "no":
    print("Physical activity is really important in your daily life, consider exercising at least 3 times a week.")
if social == "no":
  print("Social interaction is important in your daily life, consider talking to people a little bit more")
if diet == "no":
  print("A balanced diet is essential for your mental health, try to eat better")
if meditation == "no":
  print("Meditation can really help to cope with stress or anxiety.")
if outside == "no":
  print("You should spend more time on the outside")
if friends == "no":
  print("Going out with friends is important, take time of your day to stay in touch")
