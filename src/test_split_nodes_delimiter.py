import unittest

from textnode import TextType, TextNode
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
  def test_only_split_text_nodes(self):
    text_node = TextNode("**This is bold text** followed by regular text", TextType.TEXT)
    code_node = TextNode("print('**hello world**')", TextType.CODE)
    new_nodes = split_nodes_delimiter([text_node, code_node], "**", TextType.BOLD)
    self.assertEqual(len(new_nodes), 3)
    self.assertEqual(new_nodes[0].text, "This is bold text")
    self.assertEqual(new_nodes[0].text_type, TextType.BOLD)
    self.assertEqual(new_nodes[1].text, " followed by regular text")
    self.assertEqual(new_nodes[1].text_type, TextType.TEXT)
    self.assertEqual(new_nodes[2], code_node)

  def test_starts_with_delimiter(self):
    node = TextNode("**This is bold text** followed by regular text", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertEqual(len(new_nodes), 2)
    self.assertEqual(new_nodes[0].text, "This is bold text")
    self.assertEqual(new_nodes[0].text_type, TextType.BOLD)
    self.assertEqual(new_nodes[1].text, " followed by regular text")
    self.assertEqual(new_nodes[1].text_type, TextType.TEXT)

  def test_ends_with_delimiter(self):
    node = TextNode("Here is some **bold text**", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertEqual(len(new_nodes), 2)
    self.assertEqual(new_nodes[0].text, "Here is some ")
    self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
    self.assertEqual(new_nodes[1].text, "bold text")
    self.assertEqual(new_nodes[1].text_type, TextType.BOLD)

  def test_no_delimiters(self):
    node = TextNode("This is text with no delimiters", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    self.assertEqual(len(new_nodes), 1)
    self.assertEqual(new_nodes[0].text, "This is text with no delimiters")
    self.assertEqual(new_nodes[0].text_type, TextType.TEXT)

  def test_missing_closing_delimiter(self):
    node = TextNode("This is text with a `missing delimiter", TextType.TEXT)
    self.assertRaises(Exception, lambda: split_nodes_delimiter([node], "`", TextType.CODE))

  def test_italic(self):
    node = TextNode("This is text with a _italic_ word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    self.assertEqual(len(new_nodes), 3)
    self.assertEqual(new_nodes[0].text, "This is text with a ")
    self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
    self.assertEqual(new_nodes[1].text, "italic")
    self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)
    self.assertEqual(new_nodes[2].text, " word")
    self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

  def test_bold(self):
    node = TextNode("This is text with a **bold** word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertEqual(len(new_nodes), 3)
    self.assertEqual(new_nodes[0].text, "This is text with a ")
    self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
    self.assertEqual(new_nodes[1].text, "bold")
    self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
    self.assertEqual(new_nodes[2].text, " word")
    self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

  def test_code(self):
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(len(new_nodes), 3)
    self.assertEqual(new_nodes[0].text, "This is text with a ")
    self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
    self.assertEqual(new_nodes[1].text, "code block")
    self.assertEqual(new_nodes[1].text_type, TextType.CODE)
    self.assertEqual(new_nodes[2].text, " word")
    self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
    """
    new_nodes should equal
    [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" word", TextType.TEXT),
    ]
    """

if __name__ == "__main__":
  unittest.main()