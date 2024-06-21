

from flask import Flask, request, jsonify, render_template
from sql_connection import get_sql_connection
import json
import mysql.connector
import products_dao
import orders_dao
import uom_dao

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getProducts', methods=['GET'])
def get_products():
    response = products_dao.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({'product_id': product_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({'order_id': order_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({'product_id': return_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# @app.route('/deleteOrder', methods=['POST'])
# def delete_order():
#     order_id = request.json['order_id']
#     cursor = connection.cursor()

#     try:
#         # First, delete related rows in order_details table
#         cursor.execute("DELETE FROM order_details WHERE order_id = %s", (order_id,))
#         # Then, delete the order in orders table
#         cursor.execute("DELETE FROM orders WHERE order_id = %s", (order_id,))
#         connection.commit()
#         response = jsonify({'status': 'success'})
#     except mysql.connector.Error as err:
#         connection.rollback()
#         response = jsonify({'status': 'error', 'message': str(err)})
#     finally:
#         response.headers.add('Access-Control-Allow-Origin', '*')
#         cursor.close()

#     return response


def delete_order_page():
    return render_template('delete.html')

@app.route('/deleteOrder', methods=['POST'])
def delete_order():
    request_payload = request.json
    order_number = request_payload['order_number']
    order_amount = request_payload['order_amount']  # Optional: Use this for validation if needed

    # Implement deletion logic in orders_dao or wherever your order deletion function resides
    result = orders_dao.delete_order_by_number(connection, order_number)

    if result:
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error', 'message': 'Failed to delete order'})
    

    

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)
