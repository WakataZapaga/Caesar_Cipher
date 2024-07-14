from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

def caesar_cipher(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    return result

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    message = data.get('message', '')
    shift = data.get('shift', 3)
    encrypted_message = caesar_cipher(message, shift)
    return jsonify({"result": encrypted_message})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    message = data.get('message', '')
    shift = data.get('shift', 3)
    decrypted_message = caesar_cipher(message, -shift)
    return jsonify({"result": decrypted_message})

if __name__ == '__main__':
    app.run(debug=True)