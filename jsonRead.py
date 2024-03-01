# JsonRead.py
import json

def read_orders(file_name='example_orders.json'):
    # Open and read the JSON file
    with open(file_name, 'r') as file:
        orders = json.load(file)
    return orders

