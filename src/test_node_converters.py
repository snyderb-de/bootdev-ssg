import unittest
from textnode import TextNode, TextType
from node_converters import text_node_to_html_node
from leafnode import LeafNode
from htmlnode import HTMLNode

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_normal_text(self):
        text_node = TextNode("Normal text", TextType.NORMAL)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Normal text")

    def test_bold_text(self):
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")

    def test_italic_text(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")

    def test_code_text(self):
        text_node = TextNode("Code text", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code text")

    def test_link(self):
        text_node = TextNode("Click here", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def test_image(self):
        text_node = TextNode("Alt text", TextType.IMAGES, "https://example.com/image.jpg")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://example.com/image.jpg", "alt": "Alt text"})

    def test_link_without_url(self):
        text_node = TextNode("Click here", TextType.LINK)
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

    def test_image_without_url(self):
        text_node = TextNode("Alt text", TextType.IMAGES)
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

    def test_invalid_text_type(self):
        class InvalidTextType:
            pass

        text_node = TextNode("Invalid", InvalidTextType())
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

    def test_non_text_node_input(self):
        with self.assertRaises(TypeError):
            text_node_to_html_node("This is not a TextNode")


if __name__ == "__main__":
    unittest.main()
