from PIL import Image

width = 64
height = 64

# Create a new black image
black_image = Image.new("RGB", (width, height), (255, 255, 255))

# Save the black image
black_image.save("white.jpg")

print("Black image created successfully.")