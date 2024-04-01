import base64

def encode_cookie_steganography(message):
    # First, we encode the message using base64
    encoded_message = base64.b64encode(message.encode()).decode()
    # Then, we create a cookie string with a random value and the encoded message
    cookie_string = f"secret=random_value; expires=Wed, 09-Jun-2032 03:20:19 GMT"
    # We replace the random value with the encoded message
    cookie_string = cookie_string.replace("random_value", encoded_message)
    # Finally, we return the cookie string
    return cookie_string

def decode_cookie_steganography(cookie_string):
    # We extract the encoded message from the cookie string
    start_index = cookie_string.index("secret=") + len("secret=")
    end_index = cookie_string.index("; expires")
    encoded_message = cookie_string[start_index:end_index]
    # Then, we decode the encoded message
    message = base64.b64decode(encoded_message.encode()).decode()
    # Finally, we return the message
    return message

# Test the encode/decode functions
message = "I'm Exhausted"
encoded_cookie = encode_cookie_steganography(message)
decoded_message = decode_cookie_steganography(encoded_cookie)

print("Original message:", message)
print("Encoded cookie:", encoded_cookie)
print("Decoded message:", decoded_message)
