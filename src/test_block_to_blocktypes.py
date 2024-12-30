import unittest
from blocks_to_blocktypes import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), "heading")
        self.assertEqual(block_to_block_type("###### Subheading"), "heading")

    def test_code_block(self):
        self.assertEqual(block_to_block_type("```\nCode here\n```"), "code")

    def test_quote_block(self):
        self.assertEqual(block_to_block_type("> Quote\n> Another line"), "quote")

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("* Item 1\n* Item 2"), "unordered_list")
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), "unordered_list")

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. First item\n2. Second item"), "ordered_list")

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is a normal paragraph."), "paragraph")

    def test_mixed_unordered_list(self):
        block = "* Item 1\n- Item 2\n* Item 3"
        self.assertNotEqual(block_to_block_type(block), "unordered_list")

    def test_mixed_ordered_list(self):
        block = "1. Item 1\n2. Item 2\n3 Item 3 (missing period)"
        self.assertNotEqual(block_to_block_type(block), "ordered_list")

if __name__ == "__main__":
    unittest.main()
