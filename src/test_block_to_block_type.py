import unittest
from block_to_block_type import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
  def test_empty(self):
    result = block_to_block_type("")
    self.assertEqual(result, BlockType.PARAGRAPH)

  def test_paragraph(self):
    result = block_to_block_type("this is a paragraph")
    self.assertEqual(result, BlockType.PARAGRAPH)

  def test_code(self):
    result = block_to_block_type("""```
this is a code
```""")
    self.assertEqual(result, BlockType.CODE)

  def test_quote(self):
    result = block_to_block_type("""> one line
> two line
> three line""")
    self.assertEqual(result, BlockType.QUOTE)

  def test_unordered_list(self):
    result = block_to_block_type("""- one line
- two line
- three line""")
    self.assertEqual(result, BlockType.UNORDERED_LIST)

  def test_ordered_list(self):
    result = block_to_block_type("""1. one line
2. two line
3. three line""")
    self.assertEqual(result, BlockType.ORDERED_LIST)
