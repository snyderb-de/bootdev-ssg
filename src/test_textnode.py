import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_same_values(self):
        # Test when all properties are the same
        node1 = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        self.assertEqual(node1, node2)

    def test_eq_different_url(self):
        # Test when URLs are different
        node1 = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://another.com")
        self.assertNotEqual(node1, node2)

    def test_eq_different_text_type(self):
        # Test when text_type properties are different
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_eq_url_none(self):
        # Test when URL is None
        node1 = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.NORMAL, None)
        self.assertEqual(node1, node2)

    def test_eq_different_text(self):
        # Test when text properties are different
        node1 = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a different text", TextType.NORMAL)
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()