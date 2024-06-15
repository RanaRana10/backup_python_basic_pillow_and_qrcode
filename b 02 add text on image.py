from PIL import Image, ImageDraw, ImageFont

# Open an image
image_path = "logo.png"  # Replace with the path to your image
img = Image.open(image_path)

# Initialize the drawing context
draw = ImageDraw.Draw(img)

# Use a larger default font
font_size = 36  # Choose your desired font size
font = ImageFont.load_default(size=font_size)

font_path = "freemonobold.ttf"  # Replace with the path to your emoji-supporting font
font_path = "arial.ttf"  # Replace with the path to your emoji-supporting font
# font_path = "noto2.ttf"  # Replace with the path to your emoji-supporting font
font_size = 36  # Choose your desired font size
font = ImageFont.truetype(font_path, font_size)



text_color = (0, 255, 0)  # Green color, you can choose your own color
text_content = "Rana Universe😢👮‍♂️🍌 "

# Get the bounding box of the text
bbox = draw.textbbox((0, 0), text_content, font=font)
# Calculate the width and height of the text
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
print(bbox)



# Calculate the starting position to center the text horizontally
# text_position = ((img.width - text_width) // 2,10)  # Centered horizontally, 10 is the vertical position
text_position = ((img.width - text_width) // 2,10)  # Centered horizontally, 10 is the vertical position
print(text_position)
# Draw text on the image
draw.text(text_position, text_content, font=font, fill=text_color)




# Save the image with the added text
img.save("bbb4.png")
# Display the image
img.show()
