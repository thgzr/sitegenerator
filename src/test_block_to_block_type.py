import unittest
from block_to_block_type import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    
    def test_paragraph(self):
        block = "This is a simple paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
        block = "This is a multi-line\nparagraph that doesn't match\nany other block type."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_heading(self):
        block = "# Heading 1"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        
        block = "## Heading 2"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        
        block = "###### Heading 6"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        
        # Should be paragraph, not heading (no space after #)
        block = "#NoSpace"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_code(self):
        block = "```\ndef hello():\n    print('Hello, world!')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        
        # Just backticks, still a code block
        block = "```\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    
    def test_quote(self): 
        block = ">This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        
        block = ">This is a\n>multi-line quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        
        # Not a quote block because the second line doesn't start with >
        block = ">This is a\nBroken quote"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_unordered_list(self):
        block = "- Item 1"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        
        block = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        
        # Not an unordered list because the second line doesn't start with -
        block = "- Item 1\nNot an item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
        # Not an unordered list because there's no space after -
        block = "-Item 1"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_quote(self):
        block = ">This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        
        block = ">This is a\n>multi-line quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        
        # Not a quote block because the second line doesn't start with >
        block = ">This is a\nBroken quote"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_unordered_list(self):
        block = "- Item 1"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        
        block = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        
        # Not an unordered list because the second line doesn't start with -
        block = "- Item 1\nNot an item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
        # Not an unordered list because there's no space after -
        block = "-Item 1"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_ordered_list(self):
        block = "1. Item 1"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        
        block = "1. Item 1\n2. Item 2\n3. Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        
        # Not an ordered list because the second line doesn't follow the sequence
        block = "1. Item 1\n3. Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
        # Not an ordered list because it doesn't start with 1
        block = "2. Item 2\n3. Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
        # Not an ordered list because there's no space after the dot
        block = "1.Item 1"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_edge_cases(self):
        # Empty block
        block = ""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
        # Mixed blocks should be paragraphs
        block = "# Heading\n- List item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
        # Block with more than 6 # characters is a paragraph
        block = "####### Not a heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
        # Code block with content not properly closed
        block = "```\nCode without closing backticks"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()