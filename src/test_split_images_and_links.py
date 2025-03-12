import unittest
from textnode import TextNode, TextType
from split_images_and_links import split_nodes_image, split_nodes_link

### Links tests

class TestSplitNodes(unittest.TestCase):
    
    def test_split_nodes_link_single(self):
        node = TextNode("Here is [a link](https://boot.dev)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
        [
            TextNode("Here is ", TextType.TEXT),
            TextNode("a link", TextType.LINK, "https://boot.dev")
        ],
        new_nodes
    )

    def test_split_nodes_link_empty(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    def test_split_links_multiple(self):
        node = TextNode(
            "This is text with an [link text](https://www.google.com) and another [link text number 2](https://yahoo.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link text", TextType.LINK, "https://www.google.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                "link text number 2", TextType.LINK, "https://yahoo.com"
                ),
            ],
            new_nodes,
        )

    def test_split_links_no_links(self):
        node = TextNode(
            "This is text with an no link at all",
            TextType.TEXT,
     )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [TextNode("This is text with an no link at all", TextType.TEXT)], new_nodes)
    
    
    def test_split_links_consecutive(self):
        node = TextNode(
            "Start [link1](url1)[link2](url2) end",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Start ", TextType.TEXT),
                TextNode("link1", TextType.LINK, "url1"),
                TextNode("link2", TextType.LINK, "url2"),
                TextNode(" end", TextType.TEXT)            
            ],
            new_nodes,
        )

### Images tests

    def test_split_nodes_images_single(self):
        node = TextNode("Here is ![an image](https://imgur.com/random.jpg)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Here is ", TextType.TEXT),
                TextNode("an image", TextType.IMAGE, "https://imgur.com/random.jpg")
            ],
            new_nodes
        )

    def test_split_nodes_images_empty(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)

    def test_split_images_multiple(self):
        node = TextNode(
            "This is text with an ![image2](https://imgur.com/random2.jpg) and another ![image3](https://imgur.com/random3.jpg)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image2", TextType.IMAGE, "https://imgur.com/random2.jpg"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "image3", TextType.IMAGE, "https://imgur.com/random3.jpg"
                ),
            ],
            new_nodes,
        )

    def test_split_images_no_images(self):
        node = TextNode(
            "This is text with an no images at all",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("This is text with an no images at all", TextType.TEXT)], new_nodes)
    
    
    def test_split_images_consecutive(self):
        node = TextNode(
            "Start ![image1](url1)![image2](url2) end",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Start ", TextType.TEXT),
                TextNode("image1", TextType.IMAGE, "url1"),
                TextNode("image2", TextType.IMAGE, "url2"),
                TextNode(" end", TextType.TEXT)            
            ],
            new_nodes,
    )
        
if __name__ == "__main__":  # This is sometimes needed
    unittest.main()