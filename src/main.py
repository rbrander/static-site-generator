import shutil
from generate_page import generate_page

def copyDirectory(source:str, destination:str):
    print(f"Copying content from {source} to {destination}")
    shutil.rmtree(destination)
    shutil.copytree(source, destination)

def main():
    copyDirectory("./static", "./public")
    generate_page("./content/index.md", "template.html", "public/index.html")

main()
