import re

def extract_markdown_images(text):
    # Updated regex to handle nested brackets in alt text
    pattern = r"!\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\(([^()]+)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    # Updated regex to handle nested brackets in anchor text
    pattern = r"(?<!!)\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\(([^()]+)\)"
    matches = re.findall(pattern, text)
    return matches
