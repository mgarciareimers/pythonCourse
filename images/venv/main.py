from PIL import Image, ImageFilter
from utilities import utilities


# image = Image.open('./assets/bulbasur.jpg')

# Get some attributes.
# print(f'Name: { image.filename }')
# print(f'Size: { image.size }')
# print(f'Format: { image.format }')
# print(f'Mode: { image.mode }')

# Blur the image.
# blurred_image = image.filter(ImageFilter.BLUR)
# blurred_image.save('./results/blur.png', 'png')

# Smooth the image.
# smoothed_image = image.filter(ImageFilter.SMOOTH)
# smoothed_image.save('./results/smooth.png', 'png')

# Convert image to grayscale.
# gray_image = image.convert('L')
# gray_image.save('./results/gray.png', 'png')

# Rotate image and show it.
# crooked = image.rotate(90)
# crooked.show()

# Resize image to the half.
# resized = image.resize((int(image.size[0] * 0.5), int(image.size[1] * 0.5)))
# resized.save('./results/resized.png', 'png')

# Crop image.
# box = (0, (int(image.size[0] * 0.1)), (int(image.size[0] * 0.7)), (int(image.size[0] * 0.7)))
# cropped = image.crop(box)
# cropped.save('./results/cropped.png', 'png')

# Reduce size of image
# image = Image.open('./assets/dwinanda.jpg')
# image_copy = image.copy()
# image_copy.thumbnail((400, 200))
# image_copy.save('./results/dwinanda2.png', 'png')
# print(f'Size: { image_copy.size }')

# Transform JPG to PNG.
utilities.transform_jpg_to_png('./assets', './new')
