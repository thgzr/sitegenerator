import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, TextType, text_node_to_html_node
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
       # node = HTMLNode(tag = "tag a", value = "this is a test message for node 1", children = [], props = {"href": "google.com"})
       # node2 = HTMLNode(tag = "tag b", value = "this is a test message for node 2", children = [], props = {"href": "yahoo.com"})
       # node3 = HTMLNode(tag = "tag c", value = "this is a test message for node 3", children = [], props =  {"target": "_blank"})

       # print(node)
       # print(node2)
       # print(node3)

       # print(node.props_to_html())
       # print(node2.props_to_html())
       # print(node3.props_to_html())

       # node4 = LeafNode("p", "This is a paragraph of text.")
       # node5 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
       # node6 = LeafNode("d", "This is a test message", {"href": "https://www.yahoo.com"} )

       # print(node4.to_html())
       # print(node5.to_html())
       # print(node6.to_html())

        parent_node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
        print(parent_node.to_html())

        parent_node_no_children = ParentNode("aaa", None)
        print("No children test: ", parent_node_no_children.to_html())

        parent_node_no_tag = ParentNode("test", [
            LeafNode("z", "No Tag No Tag"),
            LeafNode(None, "Tag No text"),
            LeafNode("x", "tyuiytui"),
            LeafNode(None, "asdgf"),
        ])
        #print("No tag test: ", parent_node_no_tag.to_html())

        parent_node_multiple_nested_children = ParentNode("a", [
            ParentNode("z", [LeafNode("nested_child1 tag", "nested_child1 text"), LeafNode("nested_child2 tag", "nested_child2 text")]),
            LeafNode(None, "Tag No text"),
            LeafNode("x", "tyuiytui"),
            LeafNode(None, "asdgf"),
        ])
        print("Multiple children test: ", parent_node_multiple_nested_children.to_html())
   
        text_node1 = TextNode()


if __name__ == "__main__":
    unittest.main()