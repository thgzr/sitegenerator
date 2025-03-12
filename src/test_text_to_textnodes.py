import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_text_to_textnodes(self):
        old_nodes = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        result = text_to_textnodes(old_nodes)
        self.assertEqual(result, expected)

    # 1. Edge case: Empty string
    def test_empty_string(self):
        text = ""
        expected = []  # No nodes should be created
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    # 2. Edge case: Plain text without formatting
    def test_plain_text(self):
        text = "Just some plain old text."
        expected = [TextNode("Just some plain old text.", TextType.TEXT)]  # Single plain text node
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    # 3. Edge case: Text with only one formatting type
    def test_single_formatting(self):
        text = "**BoldText**"
        expected = [TextNode("BoldText", TextType.BOLD)]  # Correctly parses bold text
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    # 6. Edge case: Text with invalid syntax (unmatched tokens)
    def test_unmatched_tokens(self):
        text = "This is **bold text without end"
        with self.assertRaises(Exception) as context:
            text_to_textnodes(text)
        self.assertEqual(
            str(context.exception),
            "Invalid markdown syntax: unmatched delimiters"
    )

    # 7. Edge case: Multiple image nodes
    def test_multiple_images(self):
        text = "Here is one ![first image](https://example.com/1.jpg) and another ![second image](https://example.com/2.jpg)"
        expected = [
            TextNode("Here is one ", TextType.TEXT),
            TextNode("first image", TextType.IMAGE, "https://example.com/1.jpg"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://example.com/2.jpg"),
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

     # 8. Edge case: Combining all supported formatting types in one text
    def test_combined_formatting(self):
        text = "**Bold**, _Italic_, `Code`, ![Image](https://example.com/image.jpg), and [Link](https://example.com)"
        expected = [
            TextNode("Bold", TextType.BOLD),
            TextNode(", ", TextType.TEXT),
            TextNode("Italic", TextType.ITALIC),
            TextNode(", ", TextType.TEXT),
            TextNode("Code", TextType.CODE),
            TextNode(", ", TextType.TEXT),
            TextNode("Image", TextType.IMAGE, "https://example.com/image.jpg"),
            TextNode(", and ", TextType.TEXT),
            TextNode("Link", TextType.LINK, "https://example.com"),
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

     # 9. Edge case: Text with malformed link syntax
    def test_malformed_link(self):
        text = "[Link without closing parentheses](https://example.com"
        expected = [TextNode("[Link without closing parentheses](https://example.com", TextType.TEXT)]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    # 10. Edge case: Text with malformed image syntax
    def test_malformed_image(self):
        text = "![Image without closing parentheses(https://example.com"
        expected = [TextNode("![Image without closing parentheses(https://example.com", TextType.TEXT)]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    # 11. Edge case: Text with no spacing around formats
    def test_concatenated_formats(self):
        text = "**Bold**_Italic_`Code`"
        expected = [
            TextNode("Bold", TextType.BOLD),
            TextNode("Italic", TextType.ITALIC),
            TextNode("Code", TextType.CODE),
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)