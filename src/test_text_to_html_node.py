import unittest
import pytest

from htmlnode import HTMLNode, LeafNode 
from textnode import TextNode, TextType
from text_to_html_node import text_node_to_html_node

class TestTextToHTMLNode(unittest.TestCase):
    def test_text_node_to_html_node_basic_text(self):
        text_node = TextNode("Hello, world!", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        assert html_node.value == "Hello, world!"
        assert html_node.tag == None
        assert html_node.props == {}

    def test_text_node_to_html_node_bold_text(self):
        text_node = TextNode("Hello, world!", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        assert html_node.value == "Hello, world!"
        assert html_node.tag == "b"
        assert html_node.props == {}

    def test_text_node_to_html_node_italic_text(self):
        text_node = TextNode("Hello, world!", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        assert html_node.value == "Hello, world!"
        assert html_node.tag == "i"
        assert html_node.props == {}

    def test_text_node_to_html_node_code_text(self):
        text_node = TextNode("Hello, world!", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        assert html_node.value == "Hello, world!"
        assert html_node.tag == "code"
        assert html_node.props == {}

    def test_text_node_to_html_node_image_text(self):
        text_node = TextNode("This is an image", TextType.IMAGE, url="https://example.com")
        html_node = text_node_to_html_node(text_node)
        assert html_node.value == ""
        assert html_node.tag == "img"
        assert html_node.props == {"src" : text_node.url, "alt" : text_node.text}

    def test_text_node_to_html_node_link_text(self):
        text_node = TextNode("Click here", TextType.LINK, url="https://example.com")
        html_node = text_node_to_html_node(text_node)
        assert html_node.value == "Click here"
        assert html_node.tag == "a"
        assert html_node.props == {"href" : text_node.url}

    def test_text_node_to_html_node_invalid_type(self):
        text_node = TextNode("Hello, world!", "invalid_type")
        with pytest.raises(Exception):
            html_node = text_node_to_html_node(text_node)


if __name__ == "__main__":
    unittest.main()
