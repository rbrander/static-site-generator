from textnode import TextNode, TextType
from inline_markdown import extract_markdown_images

def split_nodes_image(old_nodes):
  split_nodes = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      split_nodes.append(node)
      continue

    images = extract_markdown_images(node.text)
    if len(images) == 0:
      split_nodes.append(node)
      continue

    curr_text = node.text
    for (image_alt, image_link) in images:
      results = curr_text.split(f"![{image_alt}]({image_link})", 1)
      before_text = results[0]
      if len(before_text) > 0:
        split_nodes.append(TextNode(before_text, TextType.TEXT))
      split_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
      after_text = results[1] if len(results) > 1 else ""
      curr_text = after_text
    if len(curr_text) > 0:
      split_nodes.append(TextNode(curr_text, TextType.TEXT))

  return split_nodes
