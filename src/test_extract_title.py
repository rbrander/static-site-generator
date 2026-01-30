import unittest;
from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
  def missing_heading(self):
    self.assertRaises(Exception, extract_title("nothing to see here"))

  def happy_path(self):
    heading = extract_title("# Hello")
    self.assertEqual(heading, "Hello")

  def multiline_heading(self):
    heading = extract_title("""
Markup paragraph

## heading two

- this
- is
- a list
""")
    self.assertEqual(heading, "heading two")
