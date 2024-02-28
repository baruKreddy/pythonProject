import json

# Read the existing orders from 'example_orders.json'
with open('example_orders.json', 'r') as file:
    orders = json.load(file)

# Aggregate item information
items = {}
for order in orders:
    for item in order['items']:
        item_name = item['name']
        item_price = item['price']
        if item_name in items:
            items[item_name]['orders'] += 1  # Increment the order count for the item
        else:
            items[item_name] = {'price': item_price, 'orders': 1}  # Initialize the item

# Write the aggregated item data to 'items.json'
with open('items.json', 'w') as json_file:
    json.dump(items, json_file, indent=4)

print("The items.json file has been created successfully.")
