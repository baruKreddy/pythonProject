# JSON Order Processor

## Description
This Python project processes order data from a JSON file (`example_orders.json`), extracts customer and item information, and then generates two JSON files: `customers.json` and `items.json`. `customers.json` maps phone numbers to customer names, and `items.json` details each item's price and the number of times it was ordered.

## Design and Architecture
The project is designed around three main components:
- **Order Reader**: Reads order data from `example_orders.json`, parsing customer names, phone numbers, and item details.
- **Data Aggregator**: Processes the order data to aggregate information about customers and items. It tracks the number of times each item is ordered and compiles customer data.
- **JSON File Writer**: Outputs the aggregated data into two separate files: `customers.json` for customer information and `items.json` for item details.

### How It Works
1. **Reading Data**: Initially, the script reads the JSON formatted order data.
2. **Processing Orders**: Each order's customer and item details are processed. For customers, it maps phone numbers to names. For items, it calculates the total orders and records prices.
3. **Writing JSON Files**: Finally, it generates `customers.json` and `items.json` with the processed data.
   
### Prerequisites
- Python 3.6 or higher

### Installation
No external libraries are required for this project, making the setup straightforward. Simply clone the repository to your local machine:

```bash
git clone https://github.com/baruKreddy/pythonProject

