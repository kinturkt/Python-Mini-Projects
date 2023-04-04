# Generate QR code

import qrcode
img=qrcode.make("Hello, this is our product")
img.save("QRSample.jpg")

# Read the QR code

import cv2 as cv
d=cv.QRCodeDetector()
text, _,_ =d.detectAndDecode(cv.imread("QRSample.jpg"))
print("Decoded Text is:",text)