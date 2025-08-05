from flask import Flask
import os

app = Flask(__name__)
DATA_FILE = '/data/order.txt'

@app.route('/')
def home():
    try:
        with open(DATA_FILE, 'a+') as f:
            f.write("Order accessed\n")
        return "Order Service Running with Persistent Storage"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
