import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

class TestSplitNodes(unittest.TestCase):
    def test_simple_text(self):
        node = TextNode("This is text with **bold** text", TextType.NORMAL)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is text with ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_inline_code(self):
        node = TextNode("This has a `code snippet` inside", TextType.NORMAL)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This has a ", TextType.NORMAL),
            TextNode("code snippet", TextType.CODE),
            TextNode(" inside", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_unmatched_delimiter(self):
        node = TextNode("This is **bold but incomplete", TextType.NORMAL)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_no_delimiters(self):
        node = TextNode("No delimiters here", TextType.NORMAL)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [TextNode("No delimiters here", TextType.NORMAL)]
        self.assertEqual(result, expected)

    def test_non_text_type(self):
        node = TextNode("This is bold", TextType.BOLD)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, [node])

    def test_mixed_nodes(self):
        nodes = [
            TextNode("This is **bold** text", TextType.NORMAL),
            TextNode("Plain bold text", TextType.BOLD),
        ]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.NORMAL),
            TextNode("Plain bold text", TextType.BOLD),
        ]
        self.assertEqual(result, expected)

    # Tests for split_nodes_image
    def test_single_image(self):
        node = TextNode("This is an image ![alt text](https://example.com/image.png)", TextType.NORMAL)
        result = split_nodes_image([node])
        expected = [
            TextNode("This is an image ", TextType.NORMAL),
            TextNode("alt text", TextType.IMAGES, "https://example.com/image.png"),
        ]
        self.assertEqual(result, expected)

    def test_multiple_images(self):
        node = TextNode(
            "Here is ![img1](https://example.com/1.png) and another ![img2](https://example.com/2.png)",
            TextType.NORMAL,
        )
        result = split_nodes_image([node])
        expected = [
            TextNode("Here is ", TextType.NORMAL),
            TextNode("img1", TextType.IMAGES, "https://example.com/1.png"),
            TextNode(" and another ", TextType.NORMAL),
            TextNode("img2", TextType.IMAGES, "https://example.com/2.png"),
        ]
        self.assertEqual(result, expected)

    def test_image_with_no_alt_text(self):
        node = TextNode("Image with no alt text ![](https://example.com/image.png)", TextType.NORMAL)
        result = split_nodes_image([node])
        expected = [
            TextNode("Image with no alt text ", TextType.NORMAL),
            TextNode("", TextType.IMAGES, "https://example.com/image.png"),
        ]
        self.assertEqual(result, expected)

    def test_no_images(self):
        node = TextNode("No images here", TextType.NORMAL)
        result = split_nodes_image([node])
        expected = [TextNode("No images here", TextType.NORMAL)]
        self.assertEqual(result, expected)

    # Tests for split_nodes_link
    def test_single_link(self):
        node = TextNode("This is a [link](https://example.com)", TextType.NORMAL)
        result = split_nodes_link([node])
        expected = [
            TextNode("This is a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://example.com"),
        ]
        self.assertEqual(result, expected)

    def test_multiple_links(self):
        node = TextNode(
            "Here is [link1](https://example.com/1) and another [link2](https://example.com/2)",
            TextType.NORMAL,
        )
        result = split_nodes_link([node])
        expected = [
            TextNode("Here is ", TextType.NORMAL),
            TextNode("link1", TextType.LINK, "https://example.com/1"),
            TextNode(" and another ", TextType.NORMAL),
            TextNode("link2", TextType.LINK, "https://example.com/2"),
        ]
        self.assertEqual(result, expected)

    def test_link_with_no_anchor_text(self):
        node = TextNode("Link with no anchor text [](https://example.com)", TextType.NORMAL)
        result = split_nodes_link([node])
        expected = [
            TextNode("Link with no anchor text ", TextType.NORMAL),
            TextNode("", TextType.LINK, "https://example.com"),
        ]
        self.assertEqual(result, expected)

    def test_no_links(self):
        node = TextNode("No links here", TextType.NORMAL)
        result = split_nodes_link([node])
        expected = [TextNode("No links here", TextType.NORMAL)]
        self.assertEqual(result, expected)

    def test_combined_images_and_links(self):
        node = TextNode(
            "Here is a [link](https://example.com) and an image ![img](https://example.com/image.png)",
            TextType.NORMAL,
        )
        links_result = split_nodes_link([node])
        images_result = split_nodes_image(links_result)
        expected = [
            TextNode("Here is a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and an image ", TextType.NORMAL),
            TextNode("img", TextType.IMAGES, "https://example.com/image.png"),
        ]
        self.assertEqual(images_result, expected)


if __name__ == "__main__":
    unittest.main()
