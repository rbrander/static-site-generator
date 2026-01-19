import unittest

from extract_markdown_links import extract_markdown_links


class TestExtractMarkdownImages(unittest.TestCase):
  def test_only_link_and_image(self):
    text = "[rick roll](https://i.imgur.com/aKaOqIh.gif)![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    results = extract_markdown_links(text)
    self.assertListEqual(results, [("rick roll", "https://i.imgur.com/aKaOqIh.gif")])

  def test_only_links(self):
    text = "[rick roll](https://i.imgur.com/aKaOqIh.gif)[obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    results = extract_markdown_links(text)
    self.assertListEqual(results, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

  def test_no_links(self):
    text = "This is text with no links"
    results = extract_markdown_links(text)
    self.assertListEqual(results, [])

  def test_sample(self):
    text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    results = extract_markdown_links(text)
    self.assertListEqual(results, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

  def test_extract_markdown_links(self):
    matches = extract_markdown_links(
        "This is text with an [image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
