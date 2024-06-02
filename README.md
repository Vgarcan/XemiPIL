# Image Processing Utility

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [User Experience](#user-experience)
  - [Key Principles](#key-principles)
  - [Customization and Flexibility](#customization-and-flexibility)
  - [Future Enhancements](#future-enhancements)
- [Testing](#testing)
- [Collaborative Efforts](#collaborative-efforts)
- [Current State and Future Plans](#current-state-and-future-plans)
  - [Current State](#current-state)
  - [Future Plans](#future-plans)
- [Deployment](#deployment)
- [License](#license)
- [Bugs and Challenges](#bugs-and-challenges)
- [Acknowledgement](#acknowledgement)

## Introduction

This project provides a set of Python functions to create directories, find images in a folder, delete used images, and convert images to different formats using the PIL (Pillow) library.

## Features

- Create directories
- Find images in a specified folder
- Delete images from the file system
- Convert images to different formats and save them in a specified location

## Technologies Used

- Python
- PIL (Pillow)

## Project Structure

```plaintext
image_processing_utility/
│
├── image_utility.py
├── README.md
└── requirements.txt
```

The `image_utility.py` file contains the main functions of the project:
- `create_directory(path)`
- `find_images(upload_folder, accepted_formats)`
- `clear_used_images(listed_images)`
- `save_as(source, format, save_at, quality=0)`


## User Experience

### Key Principles

The utility is designed to be simple and efficient, ensuring ease of use for basic image processing tasks.

### Customization and Flexibility

The functions provide parameters for specifying paths, accepted formats, and quality settings for image conversion, allowing users to tailor the utility to their needs.

### Future Enhancements

- Adding more image processing features (e.g., resizing, cropping)
- Providing a command-line interface for easier access
- Integrating with cloud storage solutions

## Testing

To test the functions, you can run the provided examples in the `image_utility.py` file after setting up your environment with the necessary dependencies listed in `requirements.txt`.

## Collaborative Efforts

If you wish to contribute to this project, please fork the repository and send a pull request with your improvements.

## Current State and Future Plans

### Current State

The project currently supports directory creation, image searching, deletion, and format conversion.

### Future Plans

- Implement more image processing features
- Develop a user-friendly command-line interface
- Enhance error handling and logging

## Deployment

To deploy this utility, ensure you have the necessary dependencies installed:

```sh
pip install pillow
```

You can then import the functions and use them in your project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Bugs and Challenges

If you encounter any bugs or challenges, please report them by opening an issue on the GitHub repository.

## Acknowledgement

This project utilizes the PIL (Pillow) library for image processing. Special thanks to the contributors and maintainers of this library.
