try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
import sys, os

TAG = sys.argv[1]

database = {}

for entry in os.scandir(TAG):
    if (entry.path.endswith(".jpg")):
        print("Analyzing: " + entry.path)
        output = pytesseract.image_to_string(entry.path)
        cleaned_output = output.replace("\n", "")
        print("Output: " + cleaned_output)
        database[entry.path] = cleaned_output