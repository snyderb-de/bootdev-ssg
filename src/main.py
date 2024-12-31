import os
import shutil
from generate_pages_recursive import generate_pages_recursive

def ensure_directory_exists(directory):
    """
    Ensures that the given directory exists. If not, creates it.
    """
    os.makedirs(directory, exist_ok=True)

def copy_directory(src, dest):
    """
    Recursively copies contents from the source directory to the destination directory.
    """
    # Ensure the source directory exists
    if not os.path.exists(src):
        print(f"Source directory '{src}' does not exist.")
        return

    # Iterate through all files and subdirectories in the source directory
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isfile(src_path):
            # Ensure the parent directory for the file exists
            ensure_directory_exists(os.path.dirname(dest_path))
            # Copy files
            shutil.copy(src_path, dest_path)
            print(f"Copied file: {src_path} -> {dest_path}")
        elif os.path.isdir(src_path):
            # Recursively copy subdirectories
            print(f"Processing directory: {src_path}")
            copy_directory(src_path, dest_path)

def main():
    static_directory = "static"
    public_directory = "public"
    content_directory = "content"
    template_file = "templates/template.html"

    # Step 1: Clear the public directory
    print(f"Clearing and preparing '{public_directory}'...")
    if os.path.exists(public_directory):
        shutil.rmtree(public_directory)
        print(f"Cleared destination directory '{public_directory}'.")
    os.makedirs(public_directory, exist_ok=True)
    print(f"Created destination directory '{public_directory}'.")

    # Step 2: Copy static files to public directory
    print(f"Copying static files from '{static_directory}' to '{public_directory}'...")
    copy_directory(static_directory, public_directory)
    print("Static files copied.")

    # Step 3: Generate HTML pages recursively
    print(f"Generating pages from '{content_directory}' using '{template_file}'...")
    generate_pages_recursive(content_directory, template_file, public_directory)
    print("All pages generated.")

if __name__ == "__main__":
    main()
