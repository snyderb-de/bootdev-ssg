from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_nodes(text):
    # Start with a single TextNode representing the entire input as normal text
    nodes = [TextNode(text, TextType.NORMAL)]
    
    # Process the nodes step by step through the different splitters
    nodes = split_nodes_image(nodes)  # First, split out images
    nodes = split_nodes_link(nodes)  # Then, split out links
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)  # Process bold text
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)  # Process italic text
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)  # Process inline code
    
    # Return the final list of TextNode objects
    return nodes
