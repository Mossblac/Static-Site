import shutil
import os
from md_to_html import generate_page

def copy_recursive(source, destination):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination):
        os.mkdir(destination)

    # Process each item in the source directory
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)

        if os.path.isfile(source_path):  # If it's a file, copy it
            shutil.copy(source_path, dest_path)
        elif os.path.isdir(source_path):  # If it's a folder, recurse!
            copy_recursive(source_path, dest_path)


def main():
    source = "static"
    destination = "public"

    # Delete "public" directory, if it exists
    if os.path.exists(destination):
        shutil.rmtree(destination)

    # Recreate the empty "public" directory
    os.mkdir(destination)

    # Call our recursive function to copy everything
    copy_recursive(source, destination)

    from_path = "content/index.md"
    template = "template.html"
    dest_path = "public/index.html"

    return generate_page(from_path, template, dest_path)

   

main()
