from jsonRead import read_orders
from customerJson import process_customers
from itemsJson import process_items

def main():
    # The name of the file to read from
    file_name = 'example_orders.json'
    # The names of the files to write to
    customers_file_name = 'customers.json'
    items_file_name = 'items.json'
    
    # Read the orders from the JSON file
    orders = read_orders(file_name)
    
    # Process the orders and create 'customers.json'
    process_customers(orders, customers_file_name)
    
    # Process the orders and create 'items.json'
    process_items(orders, items_file_name)

if __name__ == '__main__':
    main()
