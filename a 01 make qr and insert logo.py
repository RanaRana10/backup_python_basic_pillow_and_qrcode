'''
This make a qr code and then insert my logo.png inside center of the qr code
# pip install qrcode
# pip install pillow
'''


import qrcode
from PIL import Image, ImageOps


# Create a QR code instance
qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=15,  # Adjust the box size
    border=4,
)

text_data = "Rana Universe 🍌 i am your boss thanks for subscribe this my universe"

text_data = upi_link = "upi://pay?pa=netai15@paytm&am=59&pn=Connecting...&tn=I%20Donating%20to%20you%20for%20help%20me"


qr.add_data(text_data)
qr.make(fit=True)

# Create an image from the QR code
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
# Load your logo image
logo_path = "logo.png"
logo = Image.open(logo_path)
logo = logo.resize((qr_img.size[0] // 7, qr_img.size[1] // 7))  # Adjust the size
logo_position = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)

# Paste the logo onto the QR code
qr_img.paste(logo, logo_position)


border_width = 15
border_color = (0, 255, 0)
image_with_border = ImageOps.expand(qr_img,border = border_width, fill= border_color)

image_with_border.save("output_qr_code.png")
image_with_border.show()

