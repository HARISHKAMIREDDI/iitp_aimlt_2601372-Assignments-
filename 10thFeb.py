"""Question
You have a shopping list with items and their prices:

shopping_list = [
    {"item": "Milk", "price": 50},
    {"item": "Bread", "price": 30},
    {"item": "Eggs", "price": 60},
    {"item": "Rice", "price": 120}
]
Complete the following tasks:

Task 1: Add and Remove Items (30 points)
Add a new item {"item": "Butter", "price": 80} to the shopping list
Remove the first item from the list using .pop(0)
Print how many items are in the list now
Task 2: Calculate Total Cost (35 points)
Calculate the total cost of all items in the shopping list
Find the most expensive item and print its name and price
Print the total cost
Task 3: Create Summary Dictionary (35 points)
Create a dictionary called summary with:
"total_items": Number of items in the list
"total_cost": Total price of all items
"average_price": Average price per item (round to 2 decimals)
Print the summary dictionary"""

shopping_list = [
    {"item": "Milk", "price": 50},
    {"item": "Bread", "price": 30},
    {"item": "Eggs", "price": 60},
    {"item": "Rice", "price": 120}
]
#Add:
shopping_list.append({"item": "Butter", "price": 80})
#print(shopping_list)
#Remove:
removed_item=shopping_list.pop(0)
#print(removed_item,shopping_list)

#Calculate the total Cost:
total_cost=0
most_expensive=shopping_list[0]

for entry in shopping_list:
    total_cost+=entry["price"]

    #checking the most expensive:
    if entry["price"]>most_expensive["price"]:
        most_expensive=entry
print(f"Most Expensive: {most_expensive['item']} - {most_expensive['price']}")
print(f"Total Cost: {total_cost}")

#Summary:
summary={
    "total_items": len(shopping_list),
    "total_cost":total_cost,
    "average_price":round(total_cost/len(shopping_list),2)
}

print("Summary Dictionary: ")
print(summary)
