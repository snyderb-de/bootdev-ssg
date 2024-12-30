from textnode import TextNode, TextType
from extraction import extract_markdown_images, extract_markdown_links  # Import the functions


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        # Only process TextType.NORMAL nodes
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        
        # Split the text on the delimiter
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {node.text}")
        
        # Alternate between TextType.NORMAL and the given text_type
        for i, part in enumerate(parts):
            if i % 2 == 0:
                # Normal text
                if part:
                    new_nodes.append(TextNode(part, TextType.NORMAL))
            else:
                # Delimited text
                if part:
                    new_nodes.append(TextNode(part, text_type))
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