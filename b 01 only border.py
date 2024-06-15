from PIL import Image, ImageOps

# Open the image
img = Image.open("logo.png")

# Add a thin red border
border_width = 10
border_color = "red"
img_with_border = ImageOps.expand(img, border=(border_width, border_width, border_width, border_width), fill=border_color)

# Save or display the image with the border
img_with_border.save("image_with_border.png")
img_with_border.show()
