from PIL import Image


def compress_as(source: list, format: str, picname: str, save_at: str, quality: int = 65) -> None:
    """
    Compress an image file using the specified format and save it at the specified location.

    Parameters:
    source (list): A list with the paths to the input image files.
    format (str): The format to save the compressed image in. Supported formats are "PNG", "JPEG", and "WEBP".
    picname (str): The name of the output image file.
    save_at (str): The path to the directory where the output image file will be saved.
    quality (int, optional): The quality of the JPEG or WEBP image. Defaults to 65.

    Returns:
    None: This function does not return any value. It only saves the compressed image.

    Raises:
    IOError or ValueError: If there is an error opening or processing the image file.

    Example:
    ```
    download_route = "assets/converted-images/results/"
    imagen = "assets/converted-images/uploads/example1.png"
    format = "WebP"
    name_for_picture = "nuevo_images"
    compress_as(source=imagen, format=format, picname=name_for_picture, save_at=download_route, quality=30)
    ```
    """
    if not isinstance(source, list):
        raise TypeError("The 'source' argument must be a list of file paths.")

    for pic in source:
        try:
            img = Image.open(pic)
            if format == "PNG":
                img.save(f"{save_at}{picname}.{format.lower()}", format, optimize=True)
            elif format == "WebP" or format == "JPEG":
                img.save(f"{save_at}{picname}.{format.lower()}", format, quality=quality)
            print("image saved")
        except IOError or ValueError as err:
            print(f"Error with this file: {err}")


# TESTS SECTION 
download_route = "assets/converted-images/results/"
imgs_list = ["assets/converted-images/uploads/example1.png"]
format = "WebP"
name_for_picture = "nuevo_images"

compress_as (source=imgs_list, format=format, picname=name_for_picture, save_at=download_route, quality=65)