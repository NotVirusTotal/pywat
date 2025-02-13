# pywat/file_tools.py
import os
import shutil

def copy_file(src, dest):
    """
    Copies a file from src to dest.
    """
    shutil.copy(src, dest)

def move_file(src, dest):
    """
    Moves a file from src to dest.
    """
    shutil.move(src, dest)

def delete_file(file_path):
    """
    Deletes a file if it exists.
    """
    if os.path.exists(file_path):
        os.remove(file_path)

def list_files(directory):
    """
    Returns a list of files in the given directory.
    """
    return os.listdir(directory)

def check_permissions(file_path):
    """
    Checks if the file at file_path is readable.
    """
    return os.access(file_path, os.R_OK)
