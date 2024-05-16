from PIL import Image

def resize_image(input_image_path, output_image_path, new_size):
    """Resize the input image to the new size and save it."""
    original_image = Image.open(input_image_path)
    resized_image = original_image.resize(new_size)
    resized_image.save(output_image_path)

# Specify the input and output paths
input_image_path = r"C:\Users\ygourani\Downloads\banner-slide.jpg"
output_image_path = r"C:\Users\ygourani\Downloads\resized_image.jpg"

# Desired new size
new_size = (1600, 678)

# Resize the image
resize_image(input_image_path, output_image_path, new_size)

print("Image resized successfully!")
