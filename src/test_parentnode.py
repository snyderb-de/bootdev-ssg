import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_simple_parent_with_children(self):
        """Test a simple ParentNode with multiple LeafNode children."""
        node = ParentNode(
            "div",
            [
                LeafNode("p", "Paragraph 1"),
                LeafNode("p", "Paragraph 2"),
            ],
        )
        expected_html = "<div><p>Paragraph 1</p><p>Paragraph 2</p></div>"
        self.assertEqual(node.to_html(), expected_html)

    def test_parent_with_raw_text_children(self):
        """Test ParentNode with raw text LeafNode children."""
        node = ParentNode(
            "div",
            [
                LeafNode(None, "Raw text 1"),
                LeafNode(None, "Raw text 2"),
            ],
        )
        expected_html = "<div>Raw text 1Raw text 2</div>"
        self.assertEqual(node.to_html(), expected_html)

    def test_nested_parent_nodes(self):
        """Test nested ParentNode objects."""
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "section",
                    [
                        LeafNode("h1", "Heading"),
                        LeafNode("p", "Paragraph"),
                    ],
                ),
                LeafNode("footer", "Footer text"),
            ],
        )
        expected_html = "<div><section><h1>Heading</h1><p>Paragraph</p></section><footer>Footer text</footer></div>"
        self.assertEqual(node.to_html(), expected_html)

    def test_parent_with_props(self):
        """Test ParentNode with props (attributes)."""
        node = ParentNode(
            "div",
            [
                LeafNode("span", "Child text"),
            ],
            props={"class": "container", "id": "main"},
        )
        expected_html = '<div class="container" id="main"><span>Child text</span></div>'
        self.assertEqual(node.to_html(), expected_html)

    def test_no_tag_raises_error(self):
        """Test ParentNode with no tag raises ValueError."""
        with self.assertRaises(ValueError) as context:
            ParentNode(None, [LeafNode("b", "Bold text")])
        self.assertEqual(str(context.exception), "ParentNode must have a tag.")

    def test_no_children_raises_error(self):
        """Test ParentNode with no children raises ValueError."""
        with self.assertRaises(ValueError) as context:
            ParentNode("div", [])
        self.assertEqual(str(context.exception), "ParentNode must have children.")

    def test_deeply_nested_nodes(self):
        """Test deeply nested ParentNode objects."""
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "section",
                    [
                        ParentNode(
                            "article",
                            [
                                LeafNode("h1", "Deep Heading"),
                                LeafNode("p", "Deep Paragraph"),
                            ],
                        ),
                    ],
                ),
                LeafNode("footer", "Footer text"),
            ],
        )
        expected_html = "<div><section><article><h1>Deep Heading</h1><p>Deep Paragraph</p></article></section><footer>Footer text</footer></div>"
        self.assertEqual(node.to_html(), expected_html)

    def test_mixed_children(self):
        """Test ParentNode with mixed LeafNode and ParentNode children."""
        node = ParentNode(
            "ul",
            [
                ParentNode(
                    "li",
                    [
                        LeafNode(None, "First item"),
                    ],
                ),
                ParentNode(
                    "li",
                    [
                        LeafNode(None, "Second item"),
                    ],
                ),
            ],
        )
        expected_html = "<ul><li>First item</li><li>Second item</li></ul>"
        self.assertEqual(node.to_html(), expected_html)

    def test_empty_child_value(self):
        """Test ParentNode with an empty LeafNode child value."""
        node = ParentNode(
            "div",
            [
                LeafNode("span", ""),
            ],
        )
        expected_html = "<div><span></span></div>"
        self.assertEqual(node.to_html(), expected_html)

    def test_large_tree(self):
        """Test a large nested tree of ParentNode and LeafNode objects."""
        node = ParentNode(
            "html",
            [
                ParentNode(
                    "body",
                    [
                        ParentNode(
                            "div",
                            [
                                LeafNode("h1", "Main Heading"),
                                LeafNode("p", "Main content."),
                                ParentNode(
                                    "div",
                                    [
                                        LeafNode("p", "Nested content."),
                                    ],
                                    props={"class": "nested"},
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )
        expected_html = '<html><body><div><h1>Main Heading</h1><p>Main content.</p><div class="nested"><p>Nested content.</p></div></div></body></html>'
        self.assertEqual(node.to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()
