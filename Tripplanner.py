distance = int(input("Enter the distance in miles: "))
MPG = int(input("Enter the cars miles per gallon (MPG): "))
current_price = int(input("Enter the current price of gasoline per gallon: "))
days = int(input("Enter how may days you plan to travel: "))

total_cost = []

total_cost = (int(distance)*(int(MPG)*int(current_price)))*int(days)

print("your total cost will be", total_cost)
