from pil_script import *

# TESTS SECTION #
#################
UPLOAD_DIR = "./assets/converted-images/uploads/"
if not os.path.exists(UPLOAD_DIR):
    create_directory(UPLOAD_DIR)

DOWNLOAD_DIR = "./assets/converted-images/results/"
if not os.path.exists(DOWNLOAD_DIR):
    create_directory(DOWNLOAD_DIR)

ACCEPTED_FORMATS = (
    '.bmp', '.dib', '.eps', '.gif', '.icns', '.ico', '.im',
    '.jpeg', '.jpg', '.msp', '.pcx', '.png', '.ppm', '.sgi',
    '.spider', '.tga', '.tiff', '.webp', '.xbm'
)
CONVERSIONS_FORMATS = (
    'BMP', 'DIB', 'EPS', 'GIF', 'ICNS', 'ICO', 'IM',
    'JPEG', 'JPG', 'MSP', 'PCX', 'PNG', 'PPM', 'SGI',
    'TGA', 'TIFF', 'WebP', 'XBM'
)

# To be converted to:
chosen_format = "WebP"

IMGS_LIST = find_images(UPLOAD_DIR, ACCEPTED_FORMATS)
name_for_picture = "nuevo_images"

save_as (source=IMGS_LIST, format=chosen_format, save_at=DOWNLOAD_DIR, quality=65)