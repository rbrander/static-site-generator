"""
Example:
This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)

returns:
[
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
]
"""
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text:str):
  if len(text) == 0:
    return []

  nodes = [TextNode(text, TextType.TEXT)]
  nodes = split_nodes_image(nodes)
  nodes = split_nodes_link(nodes)
  nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)
  nodes = split_nodes_delimiter(nodes, '_', TextType.ITALIC)
  nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)
  return nodes

