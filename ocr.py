import easyocr

# Load English OCR model
reader = easyocr.Reader(['en'])

# Read text from image
result = reader.readtext('Sample.png', detail=0)

print("Extracted Text:")
for line in result:
    print(line)