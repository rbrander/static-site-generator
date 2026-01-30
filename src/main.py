import sys
import shutil
from generate_page import generate_pages_recursive

def copyDirectory(source:str, destination:str):
    print(f"Copying content from {source} to {destination}")
    shutil.rmtree(destination, ignore_errors=True)
    shutil.copytree(source, destination)

def main():
    basepath = sys.argv[1] if len(sys.argv) >= 2 else '/'
    dest_dir = "./docs"
    print('using base path: ', basepath)
    copyDirectory("./static", dest_dir)
    generate_pages_recursive("./content", "template.html", dest_dir, basepath)

main()
