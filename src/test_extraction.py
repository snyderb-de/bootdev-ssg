import unittest
from extraction import extract_markdown_images, extract_markdown_links

class TestMarkdownExtraction(unittest.TestCase):

    def test_extract_markdown_images_single(self):
        """Test single markdown image extraction."""
        text = "Here is an image ![alt text](https://example.com/image.png)"
        expected = [("alt text", "https://example.com/image.png")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_multiple(self):
        """Test multiple markdown image extractions."""
        text = "![first](https://example.com/1.png) and ![second](https://example.com/2.png)"
        expected = [("first", "https://example.com/1.png"), ("second", "https://example.com/2.png")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_empty(self):
        """Test no images present."""
        text = "This is a text without any images."
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_malformed(self):
        """Test malformed markdown image syntax."""
        text = "![missing closing parenthesis](https://example.com/image.png"
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links_single(self):
        """Test single markdown link extraction."""
        text = "This is a [link](https://example.com)."
        expected = [("link", "https://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_multiple(self):
        """Test multiple markdown link extractions."""
        text = "[first link](https://example.com/1) and [second link](https://example.com/2)"
        expected = [("first link", "https://example.com/1"), ("second link", "https://example.com/2")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_with_images(self):
        """Test links mixed with images, ensure only links are extracted."""
        text = "[link](https://example.com) and ![image](https://example.com/image.png)"
        expected = [("link", "https://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_empty(self):
        """Test no links present."""
        text = "This text has no links."
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_malformed(self):
        """Test malformed markdown link syntax."""
        text = "[missing closing parenthesis](https://example.com"
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_with_special_characters(self):
        """Test links with special characters in URLs."""
        text = "[link](https://example.com?query=1&key=value)"
        expected = [("link", "https://example.com?query=1&key=value")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_images_with_special_characters(self):
        """Test images with special characters in URLs."""
        text = "![image](https://example.com/image.png?query=1&key=value)"
        expected = [("image", "https://example.com/image.png?query=1&key=value")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links_nested(self):
        """Test nested brackets in links."""
        text = "[nested [link]](https://example.com)"
        expected = [("nested [link]", "https://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_images_nested(self):
        """Test nested brackets in images."""
        text = "![nested [image]](https://example.com/image.png)"
        expected = [("nested [image]", "https://example.com/image.png")]
        self.assertEqual(extract_markdown_images(text), expected)


if __name__ == "__main__":
    unittest.main()
