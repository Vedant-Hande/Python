import qrcode as qr
img = qr.make("https://github.com/vedant-Hande")
img.save(" QR code.png")