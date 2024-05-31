from PIL import Image
import os

def find_images(upload_folder, accepted_formats):
    """
    This function finds all images in a specified folder with accepted formats.

    Parameters:
    upload_folder (str): The path to the folder where the images are located.
    accepted_formats (tuple): A tuple of accepted image file extensions.

    Returns:
    list: A list of file paths to the found images.

    Note:
    The function uses os.listdir() to iterate through the files in the folder.
    It checks if each file's extension is in the accepted_formats tuple.
    If it is, the file's path is appended to the paths_list.
    Finally, the function returns the paths_list.
    """
    paths_list = []

    for image in os.listdir(upload_folder):
        if image.endswith(accepted_formats):
            paths_list.append(os.path.join(upload_folder, image))

    return paths_list

def compress_as(source: list, format: str, save_at: str, quality: int = 65) -> None:
    """
    This function compresses a list of images to a specified format and saves them at a given location.

    Parameters:
    source (list): A list of file paths to the images to be compressed.
    format (str): The format to which the images should be compressed. It can be 'png', 'jpeg', or 'webp'.
    save_at (str): The directory where the compressed images should be saved.
    quality (int, optional): The quality of the compressed images. It is only applicable for 'jpeg' and 'webp' formats. Default is 65.

    Returns:
    None

    Raises:
    TypeError: If the 'ource' argument is not a list of file paths.

    Note:
    The function prints 'image saved' for each successfully compressed image.
    It prints an error message for each image that encounters an IOError or ValueError.
    """
    
    if not isinstance(source, list):
        raise TypeError("The 'ource' argument must be a list of file paths.")
    else:
        for pic in source:
            try:
                img = Image.open(pic)
                if format.lower() == "png":
                    img.save(f"{save_at}{os.path.basename(pic)}-min.{format.lower()}", format, optimize=True)
                elif format.lower() == "webp" or format.lower() == "jpeg":
                    img.save(f"{save_at}{os.path.basename(pic)}-min.{format.lower()}", format, quality=quality)
                print("image saved")
            except IOError or ValueError as err:
                print(f"Error with this file: {err}")


# TESTS SECTION 
UPLOAD_DIR = "assets/converted-images/uploads/"
ACCEPTED_FORMATS = (
    '.bmp', '.dib', '.eps', '.gif', '.icns', '.ico', '.im',
    '.jpeg', '.jpg', '.msp', '.pcx', '.png', '.ppm', '.sgi',
    '.spider', '.tga', '.tiff', '.webp', '.xbm'
)
DOWNLOAD_DIR = "assets/converted-images/results/"

# To be converted to:
format = "WebP"

imgs_list = ["assets/converted-images/uploads/example1.png"]
name_for_picture = "nuevo_images"


compress_as (source=imgs_list, format=format, save_at=DOWNLOAD_DIR, quality=65)