from PIL import Image, ImageDraw, ImageFont

# Open an image
image_path = "aaa.png"  # Replace with the path to your image
img = Image.open(image_path)

# Initialize the drawing context
draw = ImageDraw.Draw(img)

# Use a larger default font
font_size = 36  # Choose your desired font size
font = ImageFont.load_default(size=font_size)

# font_path = "freemonobold.ttf"  # Replace with the path to your emoji-supporting font
# font_size = 36  # Choose your desired font size
# font = ImageFont.truetype(font_path, font_size)



text_color = (0, 255, 0)  # Green color, you can choose your own color
text_content = "Rana Universe is my boss"

# Get the bounding box of the text
bbox = draw.textbbox((0, 0), text_content, font=font)
# Calculate the width and height of the text
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
print(bbox)
print(f"Width is {text_width}\nheight is {text_height}")



# Calculate the starting position to center the text horizontally
# text_position = ((img.width - text_width) // 2,10)  # Centered horizontally, 10 is the vertical position
text_position = ((img.width - text_width) // 2,10)  # Centered horizontally, 10 is the vertical position
print(text_position)
# Draw text on the image
# draw.text(text_position, text_content, font=font, fill=text_color)




# Draw a rectangle around the text
rectangle_color = (0, 0, 255)  # Red color for the rectangle
rectangle_width = 5  # Width of the rectangle line
margin = 10  # Adjust the margin as needed
rectangle_coordinates = (
    text_position[0] - margin,
    text_position[1] - margin+10,
    text_position[0] + text_width + margin,
    text_position[1] + text_height + margin+10
)
draw.rectangle(rectangle_coordinates, outline=rectangle_color, width=rectangle_width, fill= "black")
draw.text(text_position, text_content, font=font, fill=text_color)



# Save the image with the added text
img.save("bbb4.png")
# Display the image
img.show()
