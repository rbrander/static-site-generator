import unittest
from textnode import TextNode, TextType
from split_nodes_link import split_nodes_link

class TestSplitNodesLink(unittest.TestCase):
  def test_no_images(self):
    node = TextNode("This is text without links", TextType.TEXT)
    new_nodes = split_nodes_link([node])
    self.assertListEqual(new_nodes, [node])

  def test_split_links(self):
    node = TextNode(
        "This is text with a link [google](https://www.google.com) and another [yahoo](https://www.yahoo.com)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("google", TextType.LINK, "https://www.google.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("yahoo", TextType.LINK, "https://www.yahoo.com"),
        ],
        new_nodes,
    )

  def test_split_image_and_link(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a link [google](https://google.com)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a link ", TextType.TEXT),
            TextNode("google", TextType.LINK, "https://google.com"),
        ],
        new_nodes,
    )
