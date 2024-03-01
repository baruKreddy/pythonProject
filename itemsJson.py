import json

def process_items(orders, output_file_name):
   
    
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

    # Write the aggregated item data to the specified JSON file
    try:
        with open(output_file_name, 'w') as json_file:
            json.dump(items, json_file, indent=4)
    except IOError as e:
        print(f"An error occurred while writing to {output_file_name}: {e}")
    else:
        print(f"The {output_file_name} file has been created successfully.")

