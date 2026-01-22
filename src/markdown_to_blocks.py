

def markdown_to_blocks(markdown):
  blocks = []
  if len(markdown.strip()) == 0:
    return blocks

  blocks = markdown.strip().split("\n\n")
  return blocks