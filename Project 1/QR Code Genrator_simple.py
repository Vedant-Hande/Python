import qrcode as qr
img = qr.make("hello")
img.save(" QR code.png")