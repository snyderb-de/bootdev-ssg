from htmlnode import HTMLNode
from leafnode import LeafNode  # Import LeafNode for type hinting (optional)

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag.")
        if not children:
            raise ValueError("ParentNode must have children.")
        super().__init__(tag=tag, props=props)
        self.children = children

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag.")
        if not self.children:
            raise ValueError("ParentNode must have children.")
        
        # Generate HTML by recursively calling to_html on each child
        children_html = ''.join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
