# from textnode import TextNode, TextType
# from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes

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

  #print(node)
  #print(node.to_html())

  text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
  result = text_to_textnodes(text)
  print('result:')
  for item in result:
    print(f"\t{item}")

if __name__ == "__main__":
  main()