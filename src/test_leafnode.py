import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
  def test_missing_value(self):
    node = LeafNode(tag="p", value=None)
    self.assertRaises(ValueError, node.to_html)

  def test_happy_path(self):
    node = LeafNode(tag="p", value="Hello World!", props={"color":"green"})
    self.assertEqual(node.to_html(), '<p color="green">Hello World!</p>')

  def test_missing_tag(self):
    node = LeafNode(tag=None, value="Lorem ipsum")
    self.assertEqual(node.to_html(), "Lorem ipsum")

  def test_text_node_with_props(self):
    # props should be ignored when rendering a text node (tag = None)
    node = LeafNode(tag=None, value="Lorem ipsum", props={"width": "100%", "color": "black"})
    self.assertEqual(node.to_html(), "Lorem ipsum")
