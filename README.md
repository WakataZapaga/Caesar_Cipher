# Caesar_Cipher
This is a beginner level project done as a part of my cybersecurity journey.

The repo includes HTML, CSS, JavaScript and Python code files. Along with the HTML/JS based frontend, Flask server has been used in the Python code. 
## Summary
The Flask application provides endpoints for encrypting and decrypting messages using the Caesar cipher function described in the code. The server supports Cross-Origin Resource Sharing (CORS) to allow requests from a different domain.

To install Flask and Flask-CORS: 
```pip install Flask Flask-CORS```

**Endpoints:**
_POST /encrypt_
* Request Body: JSON object with message (string) and shift (integer).
* Response: JSON object with result (encrypted message).
_POST /decrypt_
* Request Body: JSON object with message (string) and shift (integer).
* Response: JSON object with result (decrypted message).

The HTML, CSS, JS files provides a user interface to interact with the Flask server for encrypting and decrypting messages using the Caesar cipher.

**Elements:**
* Textarea (```<textarea id="message">```): Input field for the user to enter the message to be encrypted or decrypted.
* Input (```<input id="shift">```): Input field for the user to enter the shift value for the Caesar cipher.
* Buttons: Buttons to trigger the encrypt or decrypt actions.
* Result Display (```<span id="result">```): Element to display the result of the encryption or decryption.

**JavaScript Functions:**

```processMessage(action)```: Asynchronous function that:
* Reads the user input for message and shift.
* Sends a POST request to the Flask server with the message and shift.
* Updates the result display with the server's response.
