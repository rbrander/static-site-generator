# from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
  #node = TextNode("This is some anchor text",TextType.LINK ,"https://www.boot.dev")
  node = HTMLNode(tag="p", value="Hello World!", props={"color":"red"})
  print(node)

if __name__ == "__main__":
  main()