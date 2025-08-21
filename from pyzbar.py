from pyzbar.pyzbar import decode
from PIL import Image
import sys

"""

def decode_barcode(image_path):
    """
    Decodes barcodes and QR codes from the given image file.

    Args:
        image_path (str): Path to the image file.

    Returns:
        list: A list of decoded barcode data.
    """
    image = Image.open('))
    decoded_objects = decode(image)
    results = []
    for obj in decoded_objects:
        results.append({
            'type': obj.type,
            'data': obj.data.decode('utf-8'),
            'rect': obj.rect
        })
    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python from_pyzbar.py <image_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    results = decode_barcode(image_path)
    if results:
        for result in results:
            print(f"Type: {result['type']}, Data: {result['data']}, Rect: {result['rect']}")
    else:
        print("No barcodes found.")