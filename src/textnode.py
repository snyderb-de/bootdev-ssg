from enum import Enum

class TextType(Enum):
    NORMAL = "normal text"
    BOLD = "bold text"
    ITALIC = "italic text"
    CODE = "code text"
    LINK = "link text"
    IMAGES = "images text"

# create class TextNode with 3 properties: self.text, self.text_type and self.url
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __str__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    # EQ method  that returns True is all of the properties of two TextNode objects are equal
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    # REPR method that returns a string representation of the object, like this TextNode(TEXT, TEXT_TYPE, URL)
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"