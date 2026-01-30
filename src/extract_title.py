from block_to_block_type import BlockType, block_to_block_type
from markdown_blocks import markdown_to_blocks


def extract_title(markdown:str) -> str:
  blocks = markdown_to_blocks(markdown)
  for block in blocks:
    block_type = block_to_block_type(block)
    if block_type == BlockType.HEADING:
      return block.split(' ', maxsplit=1)[1]
  raise Exception("Unable to find heading!")
