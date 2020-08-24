

from PIL import Image

def fit(file_path, max_width=None, max_height=None, save_as=None):
    # Open file
    img = Image.open(file_path)

    # Store original image width and height
    w, h = img.size

    # Replace width and height by the maximum values
    w = int(max_width or w)
    h = int(max_height or h)

    # Proportinally resize
    img.thumbnail((w, h), Image.ANTIALIAS)

    # Save in (optional) 'save_as' or in the original path
    img.save(save_as or file_path)

    return True