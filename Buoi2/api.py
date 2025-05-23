from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher

app = Flask(__name__)

caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plaintext = data['plaintext']
    key = int(data['key'])
    encrypttext = caesar_cipher.encrypt_text(plaintext, key)
    return jsonify({'encrypt_message' : encrypttext})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    ciphertext = data['ciphertext']
    key = int(data['key'])
    decrypttext = caesar_cipher.decrypt_text(ciphertext, key)
    return jsonify({'encrypt_message' : decrypttext})




#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)