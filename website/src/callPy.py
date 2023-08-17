from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

@app.route('/crawl', methods=['POST'])
def crawl():
    print("Method crawl is called!!!")
    # Your code to run the Python script goes here
    # For example, you can call a specific Python file using subprocess
    result = subprocess.run(['python', '../../test.py'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')

    # Return the result to the frontend
    return jsonify({'message': 'Data crawled successfully', 'data': output})

if __name__ == '__main__':
    app.run(port=8081)  # Running the server on port 8080
