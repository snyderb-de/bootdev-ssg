import unittest
from text_to_nodes import text_to_nodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    def test_simple_text(self):
        text = "This is normal text."
        result = text_to_nodes(text)
        expected = [TextNode("This is normal text.", TextType.NORMAL)]
        self.assertEqual(result, expected)

    def test_bold_text(self):
        text = "This is **bold** text."
        result = text_to_nodes(text)
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_combined_syntax(self):
        text = "This is **bold**, *italic*, and `code`."
        result = text_to_nodes(text)
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(", ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(", and ", TextType.NORMAL),
            TextNode("code", TextType.CODE),
            TextNode(".", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_images_and_links(self):
        text = "An ![image](https://example.com/image.png) and a [link](https://example.com)."
        result = text_to_nodes(text)
        expected = [
            TextNode("An ", TextType.NORMAL),
            TextNode("image", TextType.IMAGES, "https://example.com/image.png"),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(".", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
