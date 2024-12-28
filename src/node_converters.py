from textnode import TextNode, TextType
from leafnode import LeafNode
from htmlnode import HTMLNode


def text_node_to_html_node(text_node):
    """
    Converts a TextNode to a corresponding LeafNode or raises an exception for unsupported types.

    :param text_node: TextNode object to convert
    :return: LeafNode object
    """
    if not isinstance(text_node, TextNode):
        raise TypeError("Input must be a TextNode object.")

    if text_node.text_type == TextType.NORMAL:
        # Raw text with no tag
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        # <b> tag for bold text
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        # <i> tag for italic text
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        # <code> tag for code text
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        # <a> tag for links with href prop
        if not text_node.url:
            raise ValueError("TextNode with TextType.LINK must have a valid URL.")
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGES:
        # <img> tag for images with src and alt props
        if not text_node.url:
            raise ValueError("TextNode with TextType.IMAGES must have a valid URL.")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unsupported TextType: {text_node.text_type}")
