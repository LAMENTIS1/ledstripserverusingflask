from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Variable to store the last message
last_message = None

@app.route('/send/<message>', methods=['GET'])
def send_message(message):
    global last_message
    last_message = message  # Update to the new message
    return jsonify({'message': last_message})

@app.route('/', methods=['GET'])
def display_last_message():
    return render_template('index.html')  # Serve the HTML page

@app.route('/latest', methods=['GET'])
def latest_message():
    return jsonify({'last_message': last_message})  # Return the last message as JSON

if __name__ == '__main__':
    app.run(debug=True)
