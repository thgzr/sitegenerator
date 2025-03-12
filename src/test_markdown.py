import unittest
from markdown import extract_markdown_images, extract_markdown_links

class TestMarkdownExtractor(unittest.TestCase):
    def test_extract_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("rick roll", "https://i.imgur.com/aKaOqIh.gif")])

    def test_extract_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("to boot dev", "https://www.boot.dev")])

    def test_extract_images_empty(self):
        text = ""
        result = extract_markdown_images(text)
        self.assertEqual(result, [])

    def test_extract_links_empty(self):
        text = ""
        result = extract_markdown_links(text)
        self.assertEqual(result, [])

    def test_extract_images_multiple(self):
        text = "Some text ![image1](https://i.imgur.com/aKaOqIh.gif) and ![image2](https://i.imgur.com/adttth.gif)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [
            ("image1", "https://i.imgur.com/aKaOqIh.gif"),
            ("image2", "https://i.imgur.com/adttth.gif")
        ])

    def test_extract_links_multiple(self):
        text = "Check out [Boot.dev](https://www.boot.dev) and [Google](https://www.google.com)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [
            ("Boot.dev", "https://www.boot.dev"),
            ("Google", "https://www.google.com")
        ])