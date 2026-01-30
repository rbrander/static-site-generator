from textnode import TextNode, TextType

# Given a list of text nodes, split them and assign text types to delimiter-wrapped content
def split_nodes_delimiter(old_nodes, delimiter, text_type):
  split_nodes = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      split_nodes.append(node)
      continue

    split_text = node.text.split(delimiter)
    # if the result length is 1, there was no delimiter found
    # If the result is an even number of values, that means there was an odd number of delimiters
    if len(split_text) % 2 == 0:
      raise Exception("Missing closing delimiter!")
    for i in range(len(split_text)):
      new_text = split_text[i]
      if len(new_text) == 0:
        continue
      new_text_type = TextType.TEXT if i % 2 == 0 else text_type
      split_nodes.append(TextNode(new_text, new_text_type))
  return split_nodes
