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
    inventory = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(inventory)

# Get employee data
@app.route('/api/employees')
def get_employees():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM employee_data;')
    employees = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(employees)

# Get current jobs
@app.route('/api/current_jobs')
def get_current_jobs():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM curent_jobs;')
    current_jobs = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(current_jobs)

# Get orders
@app.route('/api/orders')
def get_orders():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM orders;')
    orders = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(orders)

# Get pending jobs
@app.route('/api/pending_jobs')
def get_pending_jobs():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM pending_jobs;')
    pending_jobs = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(pending_jobs)

# Get sales records
@app.route('/api/sales_records')
def get_sales_records():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM sales_records;')
    sales_records = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(sales_records)
    
if __name__ == '__main__':
    app.run(debug=True)