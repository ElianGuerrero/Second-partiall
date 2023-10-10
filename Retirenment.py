https://replit.com/join/hdatsfzdqe-elianguerrero1
print("Retierment calculator")
current_age = int(input("Enter your current age: "))
retirement_age = int(input("Enter the age you want to retire: "))
desired_retirement_amount = int(input("Enter your desired retirement amount: "))
P = retirement_age-current_age
G = P * 12

monthly_savings = (int(desired_retirement_amount))/G

print("You need to save about", monthly_savings, "per month, to reach your retirement goal")
