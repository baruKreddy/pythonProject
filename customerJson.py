import json

def process_customers(orders, output_file_name):
    # Extract customer names and phone numbers, and create/update the customers dictionary
    customers = {}
    for order in orders:
        phone = order['phone']
        name = order['name']
        customers[phone] = name

    # Write the updated customers dictionary to 'customers.json'
    with open(output_file_name, 'w') as json_file:
        json.dump(customers, json_file, indent=4)

    print(f"The {output_file_name} file has been updated successfully.")
