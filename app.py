from flask import Flask, jsonify
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # For local development

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    return conn

# Test endpoint
@app.route('/')
def hello():
    return 'Hello from Flask!'
    
# Health check endpoint with curl https://your-service.onrender.com/healthcheck
@app.route('/healthcheck')
def healthcheck():
    return jsonify(status="healthy"), 200

# Get all customers
@app.route('/api/customers')
def get_customers():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM customer_data;')
    customers = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(customers)
    
# Get inventory
@app.route('/api/inventory')
def get_inventory():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM inventory;')
    customers = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(inventory)

if __name__ == '__main__':
    app.run(debug=True)