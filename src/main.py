# from textnode import TextNode, TextType
# from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode


def main():
  #node = TextNode("This is some anchor text",TextType.LINK ,"https://www.boot.dev")
  #node = HTMLNode(tag="p", value="Hello World!", props={"color":"red"})
  #node = LeafNode(tag="p", value="Hello World!", props={"color":"red"})

  node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
  )

  print(node)
  print(node.to_html())

if __name__ == "__main__":
  main()