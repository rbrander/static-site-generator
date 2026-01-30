import shutil
from generate_page import generate_pages_recursive

def copyDirectory(source:str, destination:str):
    print(f"Copying content from {source} to {destination}")
    shutil.rmtree(destination)
    shutil.copytree(source, destination)

def main():
    copyDirectory("./static", "./public")
    generate_pages_recursive("./content", "template.html", "./public")

main()
