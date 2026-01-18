from htmlnode import HTMLNode

class ParentNode(HTMLNode):
  def __init__(self, tag:str, children:list, props:dict = None):
    super().__init__(tag=tag, children=children, props=props)

  def to_html(self):
    if self.tag is None:
      raise ValueError("Parent Nodes require a tag")
    if self.children is None:
      raise ValueError("Parent Nodes require children")
    children_html = "".join(list(map(lambda child: child.to_html(), self.children)))
    return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

  def __repr__(self):
    return f"ParentNode(Tag={self.tag}, Children={self.children}, Props={self.props})"
