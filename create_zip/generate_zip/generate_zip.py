import os
import zipfile

from config import picture_path, output_path_mods


def generate_zip_arhive():
    zf = zipfile.ZipFile(f"{output_path_mods}\mods.zip", "w")
    for dirname, subdirs, files in os.walk(picture_path):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()