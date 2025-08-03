from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
import base64
import qrcode
from PIL import Image
from stegano import lsb
from pyzbar.pyzbar import decode
import io

# Load ECC Private Key
with open("private_key.pem", 'rb') as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

# Decryption Function
def decrypt_message():
    #  Step 1: Extract QR Code Data from Stego Image
    secret_image = "stego_image.png"
    extracted_qr_data = lsb.reveal(secret_image)

    if not extracted_qr_data:
        print(" No hidden message found.")
        return

    #  Step 2: Decode Base64 QR Code Data
    qr_image_data = base64.b64decode(extracted_qr_data)

    #  Step 3: Read QR Code without Saving File
    image = Image.open(io.BytesIO(qr_image_data))
    qr_result = decode(image)

    if not qr_result:
        print(" Failed to decode QR code.")
        return

    #  Step 4: Extract Encrypted Message
    encrypted_data = qr_result[0].data.decode()
    encrypted_int = int(encrypted_data)

    #  Step 5: Decrypt the Message Using Private Key
    shared_key = private_key.public_key().public_numbers().x
    decrypted_int = encrypted_int // shared_key

    #  Step 6: Convert Int to Base64 Message
    decrypted_base64 = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, 'big').decode()

    #  Step 7: Decode the Original Message
    decrypted_message = base64.b64decode(decrypted_base64).decode()

    #  Output the Message
    print(" Decrypted Message: ", decrypted_message)

# Call Decrypt Function
decrypt_message()
