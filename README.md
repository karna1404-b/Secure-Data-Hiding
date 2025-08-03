# teganography of Messages Encrypted With QR Code
This project implements a secure data-hiding technique using Elliptic Curve Cryptography (ECC), QR codes, and Least Significant Bit (LSB) steganography. The system encrypts a secret message, encodes it into a QR code, and embeds the QR code into a cover image to ensure data confidentiality and integrity.

## System Requirements

# Software Requirements
Operating System: Windows, Linux, or macOS
Python Version: Python 3.7+

# Hardware Requirements
Processor: Intel i3 or equivalent (minimum)
RAM: 4GB (minimum), 8GB+ recommended
Storage: At least 100MB for image and QR code storage

# Project Workflow
The project's workflow is a multi-step process designed to secure and conceal a message.

# Encryption & Concealment (Sender)
A message is encoded with Base64.
The Base64 message is encrypted using ECC.
A QR code is generated from the encrypted text.
The QR code is embedded into a cover image using LSB steganography.
The final stego image is sent to the receiver.

# Extraction & Decryption (Receiver)
The QR code is extracted from the received stego image.
The ECC ciphertext is decrypted using the private key.
The Base64 data is decoded to reveal the original message.

# Code Overview
The project consists of two primary Python scripts:

ENCRYPTION_CODE.py: This script handles the encryption and concealment process. It generates an ECC key pair, encrypts the message ("HIGH ALLERT"), creates a QR code, and hides it within the specified cover image (pexels-anjana-c-169994-674010.jpg), resulting in a stego_image.png file.

DECRYPTION_CODE2.py: This script performs the reverse operation. It loads the private key, extracts the hidden QR code from stego_image.png, decodes the QR data, and decrypts the message to reveal the original text.

# Output Example
The encryption process completes and saves the stego_image.png file. The decryption process successfully reveals the original message: HIGH ALLERT. The stego image is visually indistinguishable from the original cover image, demonstrating the effectiveness of the LSB steganography technique.

# Personal Reflections
This project was a fantastic opportunity to explore the intersection of cryptography and steganography. A key challenge was understanding the different layers of security and how to seamlessly integrate them. Working with Elliptic Curve Cryptography, generating QR codes, and implementing LSB steganography provided a deep dive into secure communication principles. The most rewarding part was seeing the end-to-end system work, from a plaintext message being transformed and hidden, to successfully extracting and decrypting it. This experience has significantly enhanced my understanding of data security and my skills in Python development.
