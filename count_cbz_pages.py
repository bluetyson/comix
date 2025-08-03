import zipfile
import os

# For CBR files, install the rarfile library:
# pip install rarfile
from rarfile import RarFile

def count_pages_cbz(file_path):
    with zipfile.ZipFile(file_path, 'r') as archive:
        image_files = [name for name in archive.namelist()
                       if name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff'))]
    return len(image_files)

def count_pages_cbr(file_path):
    with RarFile(file_path, 'r') as archive:
        image_files = [name for name in archive.namelist()
                       if name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff'))]
    return len(image_files)

def count_pages_in_directory(directory):
    total_pages = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.cbz'):
                total_pages += count_pages_cbz(os.path.join(root, file))
            elif file.lower().endswith('.cbr'):
                total_pages += count_pages_cbr(os.path.join(root, file))
    return total_pages

# Example usage:
print("CalibreComics")
total_pages = count_pages_in_directory(r'E:\CalibreComics')
print(f"Total pages in all CBZ and CBR comics: {total_pages}")
print("darkhorse")
total_pages = count_pages_in_directory(r'E:\darkhorse')
print(f"Total pages in all CBZ and CBR comics: {total_pages}")
print("2000AD")
total_pages = count_pages_in_directory(r'G:\2000AD')

print(f"Total pages in all CBZ and CBR comics: {total_pages}")
