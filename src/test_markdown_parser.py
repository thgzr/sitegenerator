import unittest
from markdown_parser import extract_title

class TestMarkdownExtractor(unittest.TestCase):
    def test_extract_title1(self):
        text = "# this is heading number one"
        result = extract_title(text)
        self.assertEqual(result, "this is heading number one")
        

    def test_extract_title2(self):
        text = "#this is also heading number two"
        result = extract_title(text)
        self.assertEqual(result, "this is also heading number two")

    def test_extract_title3(self):
        text = "                              #this is also heading number three"
        result = extract_title(text)
        self.assertEqual(result, "this is also heading number three")

    def test_extract_title4(self):
        text = '''                              ##this is not heading number three"
                                ####test heading one
                                # this is good one
                           
                           '''
        result = extract_title(text)
        self.assertEqual(result, "this is good one")
        

if __name__ == "__main__":
    unittest.main()