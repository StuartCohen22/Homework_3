from flask import Flask, render_template
import util

app = Flask(__name__)

# Global database credentials
username = 'raywu1990'
password = 'test'
host = '127.0.0.1'
port = '5432'
database = 'dvdrent'

@app.route('/')
def index():
    # Connect to the database using the util.py function
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    if cursor is None or connection is None:
        return "Error connecting to the database.", 500

    record2 = None

    try:
        # Step 1: Insert 'Cherry' into basket_a with a new unique ID
        insert_query = "INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry');"
        insert_result = util.run_and_commit_sql(cursor, connection, insert_query)
        if insert_result == -1:
            raise Exception("Failed to insert 'Cherry' into basket_a.")

        # Step 2: Delete 'Cucumber' from basket_a
        delete_query = "DELETE FROM basket_a WHERE fruit_a = 'Cucumber';"
        delete_result = util.run_and_commit_sql(cursor, connection, delete_query)
        if delete_result == -1:
            raise Exception("Failed to delete 'Cucumber' from basket_a.")

        # Step 3: Select unique items in basket_a but not in basket_b
        query = """
            SELECT fruit_a 
            FROM basket_a
            WHERE fruit_a NOT IN (SELECT fruit_b FROM basket_b);
        """
        record2 = util.run_and_fetch_sql(cursor, query)
        if record2 == -1:
            raise Exception("Failed to fetch unique fruits from basket_a.")

    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {e}", 500

    finally:
        # Disconnect from the database
        util.disconnect_from_db(connection, cursor)

    # Render the results into the template
    return render_template('index.html', log_html=record2)

if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)
