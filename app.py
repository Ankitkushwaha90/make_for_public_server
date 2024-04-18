from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    # Run the Flask app on the private IP address of the server machine
    # Ensure the server is reachable from other devices in the private network
    app.run(host='taking_your_private_ip', port=8080)
