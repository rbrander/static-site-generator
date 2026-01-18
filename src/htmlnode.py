class HTMLNode:
  def __init__(self, tag:str = None, value:str = None, children:list = None, props:dict = None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError()

  def props_to_html(self):
    if self.props is None or len(self.props) == 0:
      return ""
    total = ""
    for k, v in self.props.items():
      total += f' {k}="{v}"'
    return total

  def __repr__(self):
    return f"HTMLNode(Tag={self.tag}, Value={self.value}, Children={self.children}, Props={self.props})"

