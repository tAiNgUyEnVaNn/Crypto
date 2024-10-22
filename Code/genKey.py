import cv2

def resize_image(image_path, output_path, new_width, new_height):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Resize the image
    resized_image = cv2.resize(image, (new_width, new_height))

    # Save the resized image
    cv2.imwrite(output_path, resized_image)

# Example usage:
input_image_path = 'Team.jpg'
output_image_path = 'Team(512x512).jpg'
new_width = 512
new_height = 512

resize_image(input_image_path, output_image_path, new_width, new_height)