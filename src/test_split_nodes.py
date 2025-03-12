import unittest
from textnode import TextNode, TextType
from delimeter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_simple_split(self):
        old_nodes = [TextNode("This is **bold** text", TextType.TEXT)]
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        result = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(result, expected)

    def test_no_delimiter(self):
        old_nodes = [TextNode("This is normal text", TextType.TEXT)]
        expected = [TextNode("This is normal text", TextType.TEXT)]
        result = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(result, expected)

    def test_starting_with_delimiter(self):
        old_nodes = [TextNode("**bold** at the start", TextType.TEXT)]
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(" at the start", TextType.TEXT),
        ]
        result = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)