from markdown_blocks import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")
  markdown_content = ''
  template_content = ''
  with open(from_path, 'r', encoding='utf-8') as f:
    markdown_content = f.read()
  with open(template_path, 'r', encoding='utf-8') as f:
    template_content = f.read()
  parentHTMLNode = markdown_to_html_node(markdown_content)
  content = parentHTMLNode.to_html()
  title = extract_title(markdown_content)
  html = template_content.replace(r"{{ Title }}", title).replace(r"{{ Content }}", content)
  with open(dest_path, 'w', encoding='utf-8') as f:
    f.write(html)
