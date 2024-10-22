from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import numpy as np
from PIL import Image


def image_to_bits(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Convert the image to grayscale
    image = image.convert("L")

    # Get the pixel data
    pixel_data = list(image.getdata())

    # Convert each pixel value to binary
    bits = [format(pixel, "08b") for pixel in pixel_data]

    # Combine the binary values into a single string
    bits_string = "".join(bits)

    return bits_string


def encrypt_image(image_path, key):
    # Convert the image to bits
    bits = image_to_bits(image_path)

    # Convert the bits to binary data
    binary_data = bytearray(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))
    print(binary_data)
    # Pad the binary data to reach a multiple of 64 bits
    padded_data = pad(binary_data, DES.block_size)
    # print(padded_data)
    # Create a DES cipher object with the provided key
    des_cipher = DES.new(key, DES.MODE_ECB)

    # Encrypt the padded binary data
    encrypted_data = des_cipher.encrypt(padded_data)

    # Save the encrypted data to a new file
    encrypted_image_path = 'encrypted_image.bin'
    with open(encrypted_image_path, 'wb') as file:
        file.write(encrypted_data)

    print("Image encrypted successfully.")

# Example usage:
key = b'01234567'  # 64-bit DES key (8 bytes)
image_path = 'white.jpg'
encrypt_image(image_path, key)