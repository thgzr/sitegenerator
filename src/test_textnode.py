import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node3 = TextNode("This is node for test non equal", TextType.ITALIC)
        node4 = TextNode("This is node for test non EQUAL223", TextType.BOLD)
        self.assertNotEqual(node3, node4)

        node5 = TextNode("This is node for test non equal", TextType.ITALIC, "www.google.com")
        node6 = TextNode("This is node for test non equal", TextType.ITALIC, "www.yahoo.com")
        self.assertNotEqual(node5, node6)




if __name__ == "__main__":
    unittest.main()
