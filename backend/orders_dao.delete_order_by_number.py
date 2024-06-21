def delete_order_by_number(connection, order_number):
    try:
        cursor = connection.cursor()
        # Assuming `orders` table has an `order_number` field
        query = "DELETE FROM orders WHERE order_number = %s"
        cursor.execute(query, (order_number,))
        connection.commit()
        return True
    except Exception as e:
        print("Error deleting order:", e)
        return False
