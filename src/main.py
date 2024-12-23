# import TextNode class from textnode.py
from textnode import TextNode, TextType

# main function that creates a new TextNode object and prints it
def main():
    node = TextNode("Hello, World!", TextType.CODE, "https://www.example.com")
    print(node)


if __name__ == "__main__":
    main()

