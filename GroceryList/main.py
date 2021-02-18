#Grocery List App
import datetime
#create date time object and store current date/time
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

foods = ["Meat", "Cheese"]
print("Welcome to the Grocery List App.")
print("Current Date and Time: " + month + "/" + day + "\t" + hour + ":" + minute)
print("You currently have " + foods[0] + " and " + foods[1] + " in your list.")

#Get user input
food = input("\nType of food to add to grocery list: ")
foods.append(food.title())
food = input("\nType of food to add to grocery list: ")
foods.append(food.title())
food = input("\nType of food to add to grocery list: ")
foods.append(food.title())

#Print and sort the list
print("Here is your grocery list: ")
print(foods)
foods.sort()
print("Here is you grocery list sorted: ")
print(foods)

#Shopping for your list
print("\nSimulating Grocery Shopping...")
print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods)
buy_food = input("What food did you just buy: ").title()
foods.remove(buy_food)
print("Removing " + buy_food + " from the list...")

print("\nSimulating Grocery Shopping...")
print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods)
buy_food = input("What food did you just buy: ").title()
foods.remove(buy_food)
print("Removing " + buy_food + " from the list...")

print("\nSimulating Grocery Shopping...")
print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods)
buy_food = input("What food did you just buy: ").title()
foods.remove(buy_food)
print("Removing " + buy_food + " from the list...")

#The store is out of this item
print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods)
no_item = foods.pop()
print("\nSorry, the store is out of " + no_item + ".")
new_food = input("What food would you like instead: ").title()
food.insert(0,new_food)
print("\nHere is what remains on your grocery list: ")
print(foods)
#New food
