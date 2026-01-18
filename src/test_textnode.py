import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node, node2)

  def test_not_eq_type(self):
    node = TextNode("This is a text node", TextType.ITALIC)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertNotEqual(node, node2)

  def test_url_is_none(self):
    node = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node.url, None)

  def test_image(self):
    node = TextNode("This is an image", TextType.IMAGE, "https://www.google.com")
    self.assertEqual(node.url,"https://www.google.com")
    self.assertEqual(node.text,"This is an image")
    self.assertEqual(node.text_type,TextType.IMAGE)

if __name__ == "__main__":
  unittest.main()