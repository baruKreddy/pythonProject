import json

# Replace 'example_orders.json' with the name of your file
file_name = 'example_orders.json'

# Open and read the JSON file
with open(file_name, 'r') as file:
    orders = json.load(file)

# Example: Print the orders
for order in orders:
    print(order)
