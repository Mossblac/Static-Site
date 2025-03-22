import os
import shutil

def copy_files_recursive(source_dir_path, dest_dir_path):
    # Create the destination directory and all its parents, if it doesn't exist
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)

    # Iterate through the contents of the source directory
    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)  # Full path in source
        dest_path = os.path.join(dest_dir_path, filename)    # Full path in target
        print(f" * {from_path} -> {dest_path}")  # Debugging log

        if os.path.isfile(from_path):  # Copy the file if it is a standard file
            shutil.copy(from_path, dest_path)
        elif os.path.isdir(from_path):  # Recursively copy directories
            copy_files_recursive(from_path, dest_path)