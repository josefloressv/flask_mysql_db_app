from flask import Flask, request, jsonify
from flasgger import Swagger
from mysql.connector import Error
import os

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/', methods=['GET'])
def main():
    import mysql.connector

    try:
        db_host = os.getenv('DB_HOST', 'localhost')
        db_user = os.getenv('DB_USER', 'your_username')
        db_password = os.getenv('DB_PASSWORD', 'your_password')

        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password
        )
        if connection.is_connected():
            return jsonify({"message": f"Connected to MySQL database on host {db_host}"}), 200
    except Error as e:
        return jsonify({"error": f"Error connecting to MySQL: {str(e)}"}), 500
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
if __name__ == '__main__':
    app.run(debug=True)