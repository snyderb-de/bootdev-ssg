import os
from markdown_to_html_node import markdown_to_html_node
from extract_title_md import extract_title

def generate_page(from_path, template_path, dest_path):
    """
    Generate a full HTML page from a markdown file using a template.

    Args:
        from_path (str): Path to the markdown file.
        template_path (str): Path to the HTML template file.
        dest_path (str): Path to save the generated HTML page.
    """
    # Step 1: Log the generation process
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Step 2: Read the markdown file
    if not os.path.exists(from_path):
        raise FileNotFoundError(f"Markdown file '{from_path}' not found.")
    with open(from_path, "r", encoding="utf-8") as markdown_file:
        markdown_content = markdown_file.read()

    # Step 3: Read the template file
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template file '{template_path}' not found.")
    with open(template_path, "r", encoding="utf-8") as template_file:
        template_content = template_file.read()

    # Step 4: Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    # Step 5: Extract the title from the markdown
    title = extract_title(markdown_content)

    # Step 6: Replace placeholders in the template
    full_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    # Step 7: Write the full HTML to the destination path
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as dest_file:
        dest_file.write(full_html)

    print(f"Page successfully generated at {dest_path}")
