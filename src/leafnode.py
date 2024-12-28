from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # Ensure value is required and no children are allowed
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag=tag, value=value, props=props, children=[])

    def to_html(self):
        # Check if the node has a value
        if self.value is None:
            raise ValueError("LeafNode must have a value to render.")

        # If the tag is None, return the value as raw text
        if self.tag is None:
            return self.value

        # Render as an HTML tag
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
