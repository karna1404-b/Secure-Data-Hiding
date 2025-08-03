from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
import base64
import qrcode
from PIL import Image
from stegano import lsb
import os

# Generate ECC key pair
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

# Serialize public key
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save the private key (so you can decrypt later)
with open("private_key.pem", 'wb') as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

# Encryption Function
def encrypt_message(message):
    #  Step 1: Base64 Encode the Message
    base64_message = base64.b64encode(message.encode()).decode()

    #  Step 2: ECC Encrypt the Message
    # Generate a shared secret using public key
    shared_key = public_key.public_numbers().x
    encrypted_int = shared_key * int.from_bytes(base64_message.encode(), 'big')

    #  Step 3: Convert Encrypted Data to QR Code
    qr = qrcode.make(str(encrypted_int))
    qr.save("encrypted_qr.png")

    #  Step 4: Convert QR Code to Base64
    with open("encrypted_qr.png", 'rb') as f:
        qr_base64 = base64.b64encode(f.read()).decode()

    #  Step 5: Hide Base64 QR Code in Image
    secret = lsb.hide("pexels-anjana-c-169994-674010.jpg", qr_base64)

    secret.save("stego_image.png")

    print("Encryption Complete. Check 'stego_image.png'.")

# Encrypt the Message
encrypt_message("HIGH ALLERT")
