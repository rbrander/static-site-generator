import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
  def test_defaults(self):
    node = HTMLNode()
    self.assertEqual(node.tag, None)
    self.assertEqual(node.value, None)
    self.assertEqual(node.children, None)
    self.assertEqual(node.props, None)

  def test_empty_props(self):
    node = HTMLNode(tag="p", value="Hello World!")
    self.assertEqual(node.props_to_html(), "")

  def test_one_prop(self):
    node = HTMLNode(tag="p", value="Hello World!",  props={"color":"red"})
    self.assertEqual(node.props_to_html(), ' color="red"')

  def test_two_props(self):
    node = HTMLNode(tag="p", value="Hello World!",  props={"color":"red", "font-weight": "bold"})
    self.assertEqual(node.props_to_html(), ' color="red" font-weight="bold"')

if __name__ == "__main__":
  unittest.main()
