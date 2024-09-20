from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/send/<message>', methods=['GET'])
def send_message(message):
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run()
