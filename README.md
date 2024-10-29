# Homework_3

# Flask PostgreSQL Fruit Basket Program
This Flask app interacts with a PostgreSQL database to manage and display unique fruits from two baskets. Specifically:

- Inserts a new fruit, "Cherry", into basket_a.
- Deletes "Cucumber" from basket_a.
- Displays fruits that are unique to basket_a (not found in basket_b) on the webpage.

# Requirements
- Python with Flask and Psycopg2.
- PostgreSQL with tables basket_a and basket_b pre-configured.
  
# Usage
1. Run the app with python main.py.
2. Visit http://127.0.0.1:5000 to see the unique fruits in basket_a.
