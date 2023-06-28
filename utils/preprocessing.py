from utils.apply_filter import apply_filter
import os

"""
    Funtion to apply filter on all the images in the dataset
"""
def apply_filter_to_images_in_directory(directory_path):
    # Iterate over the subdirectories
    for subdir_name in os.listdir(directory_path):
        subdir_path = os.path.join(directory_path, subdir_name)
        if os.path.isdir(subdir_path):
            # Iterate over the files in the subdirectory
            for file_name in os.listdir(subdir_path):
                if file_name.endswith(".jpg"):  # Filter only for JPG files (modify as needed)
                    file_path = os.path.join(subdir_path, file_name)
                    apply_filter(file_path)

__all__ = ['apply_filter']
