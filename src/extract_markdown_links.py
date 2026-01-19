import re

"""
Given a string with markdown links, it will return a list of tuples containing link text and url

e.g.
text = "This is link to [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
print(extract_markdown_links(text))
# [("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
"""
def extract_markdown_links(text):
  return re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)