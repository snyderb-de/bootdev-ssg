from textnode import TextNode, TextType
from htmlnode import HTMLNode 
from parentnode import ParentNode
from blocks_to_blocktypes import block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from text_to_nodes import text_to_nodes
from split_nodes import split_nodes_image, split_nodes_link
from leafnode import LeafNode

def markdown_to_html_node(markdown):
    """Convert a full markdown document into a single parent HTMLNode."""
    blocks = markdown_to_blocks(markdown)  # Split into blocks
    children = []  # Collect all child nodes here

    for block in blocks:
        block_type = block_to_block_type(block)  # Determine block type

        if block_type == "heading":
            children.append(create_heading_node(block))
        elif block_type == "code":
            children.append(create_code_node(block))
        elif block_type == "quote":
            children.append(create_quote_node(block))
        elif block_type == "unordered_list":
            children.append(create_list_node(block, ordered=False))
        elif block_type == "ordered_list":
            children.append(create_list_node(block, ordered=True))
        else:
            children.append(create_paragraph_node(block))

    if not children:
        raise ValueError("Markdown document cannot be empty or invalid.")

    # Create the parent node now that we have children
    return ParentNode("div", children)


# Helper Functions

def create_heading_node(block):
    """Create an HTMLNode for a heading."""
    level = block.count("#")
    text = block[level + 1 :].strip()  # Strip heading marker and space
    return LeafNode(f"h{level}", text)


def create_code_node(block):
    """Create an HTMLNode for a code block."""
    code_text = block.strip("```")  # Remove backticks
    return LeafNode("code", code_text)


def create_quote_node(block):
    """Create an HTMLNode for a blockquote."""
    quote_text = "\n".join(line[1:].strip() for line in block.split("\n"))  # Remove '> '
    children = text_to_children(quote_text)
    return ParentNode("blockquote", children)


def create_list_node(block, ordered):
    """Create an HTMLNode for a list block."""
    tag = "ol" if ordered else "ul"
    list_items = []

    for line in block.split("\n"):
        item_text = line.lstrip("*-1234567890. ").strip()  # Remove list markers
        children = text_to_children(item_text)
        list_items.append(ParentNode("li", children))

    return ParentNode(tag, list_items)


def create_paragraph_node(block):
    """Create an HTMLNode for a paragraph."""
    children = text_to_children(block)
    return ParentNode("p", children)


def text_to_children(text):
    """Convert a string of text into a list of HTMLNode objects."""
    text_nodes = text_to_nodes(text)
    html_nodes = []

    for text_node in text_nodes:
        if text_node.text_type == TextType.NORMAL:
            html_nodes.append(LeafNode(None, text_node.text))  # Raw text
        elif text_node.text_type == TextType.BOLD:
            html_nodes.append(LeafNode("b", text_node.text))
        elif text_node.text_type == TextType.ITALIC:
            html_nodes.append(LeafNode("i", text_node.text))
        elif text_node.text_type == TextType.CODE:
            html_nodes.append(LeafNode("code", text_node.text))
        elif text_node.text_type == TextType.LINK:
            html_nodes.append(
                LeafNode("a", text_node.text, {"href": text_node.url})
            )
        elif text_node.text_type == TextType.IMAGES:
            html_nodes.append(
                LeafNode(
                    "img", "", {"src": text_node.url, "alt": text_node.text}
                )
            )
        else:
            raise ValueError(f"Unsupported TextType: {text_node.text_type}")

    return html_nodes


def create_code_node(block):
    """Create an HTMLNode for a code block."""
    code_text = block.strip("`").strip()  # Remove backticks and leading/trailing whitespace
    return LeafNode("code", code_text)