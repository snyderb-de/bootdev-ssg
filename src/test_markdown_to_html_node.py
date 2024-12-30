import unittest
from markdown_to_html_node import markdown_to_html_node
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_simple_paragraph(self):
        markdown = "This is a simple paragraph."
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(len(html_node.children), 1)
        self.assertEqual(html_node.children[0].tag, "p")
        self.assertEqual(html_node.children[0].children[0].value, "This is a simple paragraph.")

    def test_heading(self):
        markdown = "# Heading 1"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(len(html_node.children), 1)
        self.assertEqual(html_node.children[0].tag, "h1")
        self.assertEqual(html_node.children[0].value, "Heading 1")

    def test_code_block(self):
        markdown = "```\nprint('Hello, World!')\n```"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(html_node.children[0].value, "print('Hello, World!')")


    def test_unordered_list(self):
        markdown = "* Item 1\n* Item 2"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(len(html_node.children), 1)
        self.assertEqual(html_node.children[0].tag, "ul")
        self.assertEqual(len(html_node.children[0].children), 2)
        self.assertEqual(html_node.children[0].children[0].tag, "li")

    def test_quote_block(self):
        markdown = "> This is a quote."
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(len(html_node.children), 1)
        self.assertEqual(html_node.children[0].tag, "blockquote")

if __name__ == "__main__":
    unittest.main()
