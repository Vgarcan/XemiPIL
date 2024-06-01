from PIL import Image
import os
import time


def create_directory(path):
    """
    This function creates a directory at the specified path.

    Parameters:
    path (str): The path where the directory should be created.

    Returns:
    None

    Raises:
    Exception: If any error occurs during the creation of the directory.

    Note:
    The function uses the os.mkdir() method to create the directory.
    If the directory already exists, it will not be created again.
    If any error occurs during the creation of the directory, it will be caught and printed.
    """
    try:
        os.mkdir(path)
    except Exception as err:
        print(err)

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
    This function converts images from a given list of source paths to a specified format and saves them at a specified location.

    Parameters:
    source (list): A list of file paths to the images to be converted.
    format (str): The format to which the images should be converted.
    save_at (str): The directory where the converted images should be saved.
    quality (int, optional): The quality of the converted images. Default is 0, which means the original quality is preserved.

    Returns:
    None

    Raises:
    TypeError: If the 'ource' argument is not a list of file paths.

    Note:
    The function uses the PIL library to open and save images.
    If the 'quality' parameter is 0, the original quality is preserved.
    If the 'quality' parameter is greater than 0, the function optimizes the converted images based on the specified format.
    The function removes the original image after successful conversion.
    """

    if not isinstance(source, list):
        raise TypeError("The 'ource' argument must be a list of file paths.")
    elif len(source) == 0:
        print("No images to convert.")
        return
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
                print(pic)
                
                
            except IOError or ValueError as err:
                print(f"File: '{os.path.basename(pic)}' gave the next ERROR:\n {err}")
    


def clear_used_images(listed_images, accepted_formats):

    for image in listed_images:
        try:
            if image.endswith(accepted_formats):
                os.remove(image)
        except Exception as e:
            print(f'Problems with file {os.path.basename(image)}:\n',e)
            continue
    