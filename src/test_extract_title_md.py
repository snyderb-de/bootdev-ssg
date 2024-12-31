import unittest
from extract_title_md import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_valid_h1_title(self):
        markdown = "# Hello"
        self.assertEqual(extract_title(markdown), "Hello")

    def test_h1_with_whitespace(self):
        markdown = "#   Welcome to the World   "
        self.assertEqual(extract_title(markdown), "Welcome to the World")

    def test_no_h1_raises_exception(self):
        markdown = "## Subheading\nSome content"
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_multiple_h1_returns_first(self):
        markdown = "# First Title\n# Second Title"
        self.assertEqual(extract_title(markdown), "First Title")

    def test_ignores_invalid_h1(self):
        markdown = "This is not a title\n## Subheading\n#Valid"
        self.assertEqual(extract_title(markdown), "Valid")

    def test_empty_markdown_raises_exception(self):
        markdown = ""
        with self.assertRaises(ValueError):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()
