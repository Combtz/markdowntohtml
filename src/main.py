import os
import shutil
from mdtohtml import generate_page

def copy_directory_contents(src, dest):
    # Remove the destination directory if it exists
    if os.path.exists(dest):
        shutil.rmtree(dest)
    
    # Create the destination directory
    os.mkdir(dest)
    
    # Iterate over all items in the source directory
    for item in os.listdir(src):
        src_item = os.path.join(src, item)
        dest_item = os.path.join(dest, item)

        # If the item is a directory, recursively copy its contents
        if os.path.isdir(src_item):
            copy_directory_contents(src_item, dest_item)
        else:
            # If the item is a file, copy it to the destination
            shutil.copy(src_item, dest_item)
            print(f"Copied file: {src_item} -> {dest_item}")


def main():
    # Remove the existing 'public' directory if it exists
    if os.path.exists("public"):
        shutil.rmtree("public")

    # Copy all the static files from 'static' to 'public'
    shutil.copytree("static", "public")

    # Generate the HTML page from 'content/index.md' using 'template.html'
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
