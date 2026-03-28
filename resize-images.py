"""
Compound Class Visual Representation
Copyright (C) 2026 Nitish Kapur
GitHub: [github.com/nitish-kapur](https://github.com/nitish-kapur)
Licensed under GNU GPLv3
"""

"""
    1.  Runs automatically in the directory where the script is located —
        no file dialog is required.
    2.  Scans the folder for all supported image files:
            .jpg, .jpeg, .png, .bmp, .gif
    3.  For each image found, converts the target dimensions from inches to
        pixels using: pixels = inches × DPI.
    4.  Opens the image using Pillow and resizes it to the calculated pixel
        dimensions using the Lanczos resampling filter for high quality.
    5.  Saves the resized image in the same folder with a 'resized_' prefix
        added to the original filename (e.g. 'resized_image.png').
    6.  Original files are left unmodified.
    7.  Default output size is 14 × 8 inches at 300 DPI (4200 × 2400 px).
        Edit the values at the bottom of the script to change dimensions.
"""

import os
from PIL import Image


def resize_image(input_path, output_path, width_inch, height_inch, dpi=300):
    # Convert inches to pixels (assuming dpi of 300 for high-quality images)
    width_pixels = width_inch * dpi
    height_pixels = height_inch * dpi

    try:
        # Open the image
        with Image.open(input_path) as img:
            # Resize the image
            img_resized = img.resize((int(width_pixels), int(height_pixels)), Image.LANCZOS)

            # Save the resized image
            img_resized.save(output_path)
            print(f"Image resized and saved to {output_path}")
    except Exception as e:
        print(f"Error resizing image {input_path}: {e}")


def resize_all_images_in_folder(folder_path, width_inch, height_inch, dpi=300):
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is an image (based on extension)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            input_path = os.path.join(folder_path, filename)

            # Create output file path (optional: change extension or folder)
            output_path = os.path.join(folder_path, f"resized_{filename}")

            # Resize the image
            resize_image(input_path, output_path, width_inch, height_inch, dpi)


# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Example usage: Resize all images in the current folder to 14x10 inches at 300 DPI
resize_all_images_in_folder(current_directory, 14, 8, dpi=300)
