import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node
from extract_title import extract_title

def write_file_pathlib(file_path, content):
    """Writes content to a file, creating parent directories as needed."""
    p = Path(file_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)

def generate_page(from_path, template_path, dest_path, basepath = "/"):
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
  html = html.replace(r'href="/', f'href="{basepath}').replace(r'src="/', f'src="{basepath}')
  write_file_pathlib(dest_path, html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath = "/"):
  files = os.listdir(dir_path_content)
  for file in files:
    src_path = os.path.join(dir_path_content, file)
    if os.path.isdir(src_path):
      generate_pages_recursive(src_path, template_path, os.path.join(dest_dir_path, file), basepath)
    elif os.path.isfile(src_path):
      (filename, extension) = os.path.splitext(file)
      if extension == '.md':
        generate_page(src_path, template_path,os.path.join(dest_dir_path,filename + '.html'), basepath)
