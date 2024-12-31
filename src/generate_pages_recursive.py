import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    # Iterate through all items in the content directory
    for item in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)

        if os.path.isdir(src_path):
            # Recursively handle subdirectories
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(src_path, template_path, dest_path)
        elif os.path.isfile(src_path) and src_path.endswith(".md"):
            # Generate an HTML file for markdown files
            dest_html_path = os.path.splitext(dest_path)[0] + ".html"
            print(f"Generating page for: {src_path} -> {dest_html_path}")
            generate_page(src_path, template_path, dest_html_path)
