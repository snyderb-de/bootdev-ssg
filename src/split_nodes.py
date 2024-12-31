import re
from textnode import TextNode, TextType
from extraction import extract_markdown_images, extract_markdown_links  # Import the functions


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    delimiter_pattern = re.escape(delimiter)  # Escape special characters like *
    regex = re.compile(f"(.*?){delimiter_pattern}(.*?){delimiter_pattern}(.*)")

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        text = node.text
        while True:
            match = regex.match(text)
            if not match:
                break

            # Add text before the bold part
            if match.group(1):
                new_nodes.append(TextNode(match.group(1), TextType.NORMAL))
            # Add the bold part
            new_nodes.append(TextNode(match.group(2), text_type))
            # Continue processing the remaining text
            text = match.group(3)

        # Add remaining text if any
        if text:
            new_nodes.append(TextNode(text, TextType.NORMAL))

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        
        # Use extract_markdown_images to find images in the text
        matches = extract_markdown_images(node.text)
        text = node.text
        last_index = 0
        for match in matches:
            alt_text, url = match
            start_index = text.find(f"![{alt_text}]({url})", last_index)
            if start_index > last_index:
                # Add the preceding text
                new_nodes.append(TextNode(text[last_index:start_index], TextType.NORMAL))
            # Add the image node
            new_nodes.append(TextNode(alt_text, TextType.IMAGES, url))
            last_index = start_index + len(f"![{alt_text}]({url})")
        # Add any remaining text
        if last_index < len(text):
            new_nodes.append(TextNode(text[last_index:], TextType.NORMAL))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        # Use extract_markdown_links to find links in the text
        matches = extract_markdown_links(node.text)
        text = node.text
        last_index = 0
        for match in matches:
            anchor_text, url = match
            start_index = text.find(f"[{anchor_text}]({url})", last_index)
            if start_index > last_index:
                # Add the preceding text
                new_nodes.append(TextNode(text[last_index:start_index], TextType.NORMAL))
            # Add the link node
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            last_index = start_index + len(f"[{anchor_text}]({url})")
        # Add any remaining text
        if last_index < len(text):
            new_nodes.append(TextNode(text[last_index:], TextType.NORMAL))
    return new_nodes