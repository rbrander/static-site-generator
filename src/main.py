import shutil
from textnode import TextNode, TextType


def copyDirectory(source:str, destination:str):
    print(f"Copying content from {source} to {destination}")
    shutil.rmtree(destination)
    shutil.copytree(source, destination)

def main():
    copyDirectory("./static", "./public")


main()
