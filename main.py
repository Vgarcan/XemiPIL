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
        try:
            if image.endswith(accepted_formats):
                paths_list.append(os.path.join(upload_folder, image))
        except Exception as e:
            print(f'Problems with file {os.path.basename(image)}:\n',e)
            continue

    return paths_list

def save_as(source: list, format: str, save_at: str, quality: int = 0):
    """
    This function saves images from a list of source paths to a specified directory with a given format and quality.

    Parameters:
    source (list): A list of file paths to the images to be converted.
    format (str): The format to which the images will be converted.
    save_at (str): The directory where the converted images will be saved.
    quality (int, optional): The quality of the converted images. Default is 0, which means no compression.

    Returns:
    None

    Raises:
    TypeError: If the 'ource' argument is not a list.

    Note:
    The function uses the PIL library to open and save images.
    If the 'quality' parameter is greater than 0, the function will save the images with the specified quality.
    If the 'quality' parameter is 0, the function will save the images without any compression.
    The function will print an error message if an image cannot be saved due to an IOError or ValueError.
    """

    if not isinstance(source, list):
        raise TypeError("The 'ource' argument must be a list of file paths.")
    else:
        for pic in source:
            try:
                img = Image.open(pic)
                if quality == 0:
                    img.save(f"{save_at}{os.path.basename(pic)}.{format.lower()}", format)
                elif format.lower() == "png":
                    img.save(f"{save_at}{os.path.basename(pic)}-min.{format.lower()}", format, optimize=True)
                elif format.lower() in ["webp", "jpeg"]:
                    img.save(f"{save_at}{os.path.basename(pic)}-min.{format.lower()}", format, quality=quality)
                else:
                    print(f"The format '{format}' with 'QUALITY > 0' is not supported.\nPlease use one of the following formats with 'QUALITY > 0':\nWebP, JPEG, PNG,")
                    break
                print("image saved")
            except IOError or ValueError as err:
                print(f"File: '{os.path.basename(pic)}' gave the next ERROR:\n {err}")


# TESTS SECTION 
UPLOAD_DIR = "assets/converted-images/uploads/"
ACCEPTED_FORMATS = (
    '.bmp', '.dib', '.eps', '.gif', '.icns', '.ico', '.im',
    '.jpeg', '.jpg', '.msp', '.pcx', '.png', '.ppm', '.sgi',
    '.spider', '.tga', '.tiff', '.webp', '.xbm'
)
CONVERTIONS_FORMATS = (
    'BMP', 'DIB', 'EPS', 'GIF', 'ICNS', 'ICO', 'IM',
    'JPEG', 'JPG', 'MSP', 'PCX', 'PNG', 'PPM', 'SGI',
    'TGA', 'TIFF', 'WebP', 'XBM'
)
DOWNLOAD_DIR = "assets/converted-images/results/"

# To be converted to:
chosen_format = "WebP"

IMGS_LIST = find_images(UPLOAD_DIR, ACCEPTED_FORMATS)
name_for_picture = "nuevo_images"


save_as (source=IMGS_LIST, format=chosen_format, save_at=DOWNLOAD_DIR, quality=65)