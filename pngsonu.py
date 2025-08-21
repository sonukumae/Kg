from pyzbar.pyzbar import decode
from PIL import Image

try:
    # Load your QR code image file
    image = Image.open('qr_code.png')  # Put your file name here
except FileNotFoundError:
    print("Error: 'qr_code.png' not found in the current directory.")
    exit(1)

# Decode the QR code
decoded_objects = decode(image)

if not decoded_objects:
    print("No QR code found in the image.")
else:
    # Print the QR code data
    for obj in decoded_objects:
        print("QR Code Type:", obj.type)
        print("QR Code Data:", obj.data.decode("utf-8"))
        print("QR Code Rect:", obj.rect)