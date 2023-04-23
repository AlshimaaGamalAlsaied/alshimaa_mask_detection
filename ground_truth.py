# from PIL import Image, ImageDraw

# image = Image.open("datasets/mask/valid/images/maksssksksss844.png")

# with open("datasets/mask/valid/labels/maksssksksss844.txt", "r") as f:
#     for line in f:
#         label, x_min, y_min, x_max, y_max = line.strip().split()
#         x_min, y_min, x_max, y_max = map(float, [x_min, y_min, x_max, y_max])
        
#         draw = ImageDraw.Draw(image)
#         draw.rectangle([(x_min, y_min), (x_max, y_max)], outline="red", width=2)


# # Save the image with the drawn bounding boxes
# image.save("output.png")

import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw

image = Image.open("datasets/mask/valid/images/maksssksksss670.png")

with open("datasets/mask/valid/labels/maksssksksss670.txt", "r") as f:
   for line in f:
        # Parse the line
        label, x_center, y_center, width, height = map(float, line.strip().split())

        # Convert YOLO format coordinates to PIL-compatible coordinates
        left = int((x_center - width/2) * image.width)
        top = int((y_center - height/2) * image.height)
        right = int((x_center + width/2) * image.width)
        bottom = int((y_center + height/2) * image.height)

        # Draw the bounding box
        draw = ImageDraw.Draw(image)
        draw.rectangle([(left, top), (right, bottom)], outline="red", width=2)


image.save("output.png")
