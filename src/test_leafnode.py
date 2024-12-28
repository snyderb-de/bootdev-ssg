import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_no_tag(self):
        """Test to_html with no tag."""
        node = LeafNode(tag=None, value="Raw text")
        self.assertEqual(node.to_html(), "Raw text")
    
    def test_to_html_with_tag(self):
        """Test to_html with a valid tag and value."""
        node = LeafNode(tag="p", value="Paragraph text")
        self.assertEqual(node.to_html(), "<p>Paragraph text</p>")

    def test_to_html_with_props(self):
        """Test to_html with props."""
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click me!</a>')

    def test_to_html_missing_value(self):
        """Test to_html raises ValueError for missing value."""
        with self.assertRaises(ValueError):
            LeafNode(tag="div", value=None)

    def test_repr(self):
        """Test __repr__ method."""
        node = LeafNode(tag="span", value="Some text", props={"class": "highlight"})
        expected_repr = (
            "HTMLNode(tag='span', value='Some text', children=[], props={'class': 'highlight'})"
        )
        self.assertEqual(repr(node), expected_repr)


if __name__ == "__main__":
    unittest.main()
