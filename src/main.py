import os
import shutil

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
    src_dir = "./static"
    dest_dir = "./public"
    copy_directory_contents(src_dir, dest_dir)

if __name__ == "__main__":
    main()
