import json

# Step 1: Read the existing orders from 'example_orders.json'
with open('example_orders.json', 'r') as file:
    orders = json.load(file)

# Step 2: Extract customer names and phone numbers, and Step 3: Create/Update the customers dictionary
customers = {}
for order in orders:
    phone = order['phone']
    name = order['name']
    customers[phone] = name

# Step 4: Write the updated customers dictionary to 'customers.json'
with open('customers.json', 'w') as json_file:
    json.dump(customers, json_file, indent=4)

print("The customers.json file has been updated successfully.")
