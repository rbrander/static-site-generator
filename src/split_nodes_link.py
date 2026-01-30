from textnode import TextNode, TextType
from inline_markdown import extract_markdown_links

def split_nodes_link(old_nodes):
  split_nodes = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      split_nodes.append(node)
      continue

    links = extract_markdown_links(node.text)
    if len(links) == 0:
      split_nodes.append(node)
      continue

    curr_text = node.text
    for (link_text, link_url) in links:
      results = curr_text.split(f"[{link_text}]({link_url})", 1)
      before_text = results[0]
      if len(before_text) > 0:
        split_nodes.append(TextNode(before_text, TextType.TEXT))
      split_nodes.append(TextNode(link_text, TextType.LINK, link_url))
      after_text = results[1] if len(results) > 1 else ""
      curr_text = after_text
    if len(curr_text) > 0:
      split_nodes.append(TextNode(curr_text, TextType.TEXT))

  return split_nodes
