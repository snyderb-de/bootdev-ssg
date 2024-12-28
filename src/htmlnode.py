class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        """
        Represents an HTML element.

        Args:
        - tag (str, optional): The name of the HTML tag. Defaults to None.
        - value (str, optional): The inner text of the HTML tag. Defaults to None.
        - children (list, optional): A list of child HTMLNode objects. Defaults to None.
        - props (dict, optional): A dictionary of attributes for the HTML tag. Defaults to None.
        """
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def props_to_html(self):
        """
        Converts the props dictionary into a properly formatted HTML attribute string.

        Returns:
        str: A string representing HTML attributes, with a leading space if attributes exist.
        """
        if not self.props:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def render(self):
        """
        Renders the HTMLNode as an HTML string.

        Returns:
        str: The HTML representation of the node.
        """
        # If there is no tag, render as raw text
        if not self.tag:
            return self.value or ""

        # Get the props string
        props_str = self.props_to_html()

        # If there are children, render them recursively
        if self.children:
            children_str = "".join(child.render() for child in self.children)
            return f"<{self.tag}{props_str}>{children_str}</{self.tag}>"

        # Otherwise, render the value
        return f"<{self.tag}{props_str}>{self.value or ''}</{self.tag}>"

    def to_html(self):
        """
        Converts the node to its HTML representation.
        This method is intended to be overridden by subclasses.
        
        Raises:
            NotImplementedError: If the method is not implemented in subclasses.
        """
        raise NotImplementedError("The to_html method must be implemented in subclasses.")

    def __repr__(self):
        """
        Returns a string representation of the HTMLNode object for debugging purposes.

        Returns:
        str: A string representing the HTMLNode's tag, value, children, and props.
        """
        return (
            f"HTMLNode(tag={self.tag!r}, value={self.value!r}, "
            f"children={self.children!r}, props={self.props!r})"
        )
