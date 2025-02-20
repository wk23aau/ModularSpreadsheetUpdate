IMAGE_COLUMN_COUNT = 5 # Define IMAGE_COLUMN_COUNT here as it might be used in this module

def extract_images(images_json):
    try:
        image_list = eval(images_json)
        if isinstance(image_list, list):
            return [img.get("images-src", "") for img in image_list if isinstance(img, dict)]
    except (NameError, TypeError, SyntaxError):
        print(f"Warning: Could not parse images JSON: {images_json}")
    return [""] * IMAGE_COLUMN_COUNT