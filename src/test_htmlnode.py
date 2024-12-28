import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_no_props(self):
        """Test props_to_html with no props."""
        node = HTMLNode(tag="div")
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_with_props(self):
        """Test props_to_html with props."""
        node = HTMLNode(tag="a", props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com" target="_blank"')

    def test_props_to_html_with_single_prop(self):
        """Test props_to_html with a single prop."""
        node = HTMLNode(tag="img", props={"src": "image.jpg"})
        self.assertEqual(node.props_to_html(), ' src="image.jpg"')

    def test_render_with_children(self):
        """Test render with children nodes."""
        child_node = HTMLNode(tag="span", value="Child text")
        parent_node = HTMLNode(tag="div", children=[child_node], props={"class": "container"})
        expected_html = '<div class="container"><span>Child text</span></div>'
        self.assertEqual(parent_node.render(), expected_html)

    def test_render_no_children(self):
        """Test render with no children."""
        node = HTMLNode(tag="p", value="Paragraph text", props={"class": "text"})
        expected_html = '<p class="text">Paragraph text</p>'
        self.assertEqual(node.render(), expected_html)

    def test_render_raw_text(self):
        """Test render for raw text without a tag."""
        node = HTMLNode(value="Raw text")
        self.assertEqual(node.render(), "Raw text")

    def test_repr(self):
        """Test __repr__ method."""
        node = HTMLNode(tag="a", value="Click here", props={"href": "https://example.com"})
        expected_repr = (
            "HTMLNode(tag='a', value='Click here', children=[], props={'href': 'https://example.com'})"
        )
        self.assertEqual(repr(node), expected_repr)


if __name__ == "__main__":
    unittest.main()
