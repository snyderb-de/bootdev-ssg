import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_simple_markdown(self):
        markdown = "# This is a heading\n\nThis is a paragraph.\n\nAnother paragraph."
        expected = [
            "# This is a heading",
            "This is a paragraph.",
            "Another paragraph.",
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)
    
    def test_markdown_with_lists(self):
        markdown = (
            "* This is the first item\n"
            "* This is the second item\n\n"
            "A new paragraph here."
        )
        expected = [
            "* This is the first item\n* This is the second item",
            "A new paragraph here.",
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)
    
    def test_markdown_with_excessive_newlines(self):
        markdown = (
            "# Heading\n\n"
            "\n\n"
            "Paragraph with text.\n\n"
            "\n\n"
            "* List item\n\n"
            "* Another list item\n\n"
            "\n\n"
        )
        expected = [
            "# Heading",
            "Paragraph with text.",
            "* List item",
            "* Another list item",
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)
    
    def test_empty_markdown(self):
        markdown = "\n\n\n"
        expected = []
        self.assertEqual(markdown_to_blocks(markdown), expected)
    
    def test_markdown_with_trailing_whitespace(self):
        markdown = "  # Heading  \n\n  Paragraph  \n\n  "
        expected = [
            "# Heading",
            "Paragraph",
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

if __name__ == "__main__":
    unittest.main()
