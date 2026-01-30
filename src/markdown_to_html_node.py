from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from htmlnode import ParentNode,LeafNode
from markdown_blocks import block_to_html_node

def markdown_to_html_node(markdown):
  blocks = markdown_to_blocks(markdown)
  htmlnodes = []
  for block in blocks:
    block_to_html_node
    htmlnodes.append(block_to_html_node(block))
  return ParentNode('div', htmlnodes)

"""
def block_to_html_node(block:str):
  node = LeafNode()
  block_type = block_to_block_type(block)
  match (block_type):
    case BlockType.HEADING:
      # split on first space to get the heading identifier and the content
      [heading_identifier, content] = block.split(' ', maxsplit=1)
      heading_level = len(heading_identifier.strip())
      node = LeafNode(f"h{heading_level}", content.strip())
    case BlockType.PARAGRAPH:
      node = LeafNode(f"p", block)
    case BlockType.CODE:
      node = LeafNode(f"code", block[4:-3])
    case BlockType.QUOTE:
      content = '\n'.join(list(map(lambda line: line[2:], block.split('\n'))))
      node = LeafNode(f"blockquote", content)
    case BlockType.UNORDERED_LIST:
      list_items = list(map(lambda line: line[2:], block.split('\n')))
      list_item_nodes = list(map(lambda item: LeafNode('li', item), list_items))
      node = ParentNode("ul", list_item_nodes)
    case BlockType.ORDERED_LIST:
      list_items = list(map(
        lambda line: line.split(' ', maxsplit=1)[1],
        block.split('\n')
      ))
      list_item_nodes = list(map(lambda item: LeafNode('li', item), list_items))
      node = ParentNode("ol", list_item_nodes)
    case _:
      raise Exception("Invalid BlockType")
  return node
"""
