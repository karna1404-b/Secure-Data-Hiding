# Steganography of Messages Encrypted With QR Code
This project implements a secure data-hiding technique using ECC encryption, QR codes, and LSB steganography. The system encrypts a message, encodes it into a QR code, and embeds the code into an image. This approach ensures data confidentiality and integrity, making it suitable for secure communication.
Based on the information you provided, here is a detailed and formal content for your README.md file.

# System Requirements && Software Requirements
Operating System: Windows, Linux, or macOS 
Python Version: Python 3.7+ 

# Hardware Requirements
Processor: Intel i3 or equivalent (minimum) 
RAM: 4GB (minimum), 8GB+ recommended 
Storage: At least 100MB for image and QR code storage 

# Project Workflow
The project's workflow can be broken down into the following stages:
Encryption & Concealment (Sender)
A message is encoded with Base64.
The Base64 message is encrypted using ECC.
A QR code is generated from the encrypted text.
The QR code is embedded into a cover image using LSB steganography.
The final stego image is sent to the receiver.
Extraction & Decryption (Receiver)
The QR code is extracted from the received stego image.
The ECC ciphertext is decrypted using the private key.
The Base64 data is decoded to reveal the original message.

# Code Overview
The project consists of two primary Python scripts:

# ENCRYPTION_CODE.py
This script handles the entire encryption and concealment process. It generates an ECC key pair, encrypts a given message ("HIGH ALLERT" in the example), creates a QR code, and hides it within a specified image ("pexels-anjana-c-169994-674010.jpg"). The output is a stego_image.png file.

# DECRYPTION_CODE2.py
This script performs the reverse operation. It loads the private key, extracts the hidden QR code from stego_image.png, decodes the QR data, and decrypts the message to reveal the original text.

# Output Example
The encryption process completes and saves the stego_image.png. The decryption process successfully reveals the original message: 
HIGH ALLERT. The stego image is visually indistinguishable from the original cover image, demonstrating the effectiveness of the LSB steganography technique.
