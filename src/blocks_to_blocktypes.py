def block_to_block_type(block):
    # Check for headings (1-6 # followed by a space)
    if block.startswith("# "):
        return "heading"
    elif block.startswith("## "):
        return "heading"
    elif block.startswith("### "):
        return "heading"
    elif block.startswith("#### "):
        return "heading"
    elif block.startswith("##### "):
        return "heading"
    elif block.startswith("###### "):
        return "heading"

    # Check for code blocks (start and end with 3 backticks)
    if block.startswith("```") and block.endswith("```"):
        return "code"

    # Check for quote block (every line starts with >)
    if all(line.strip().startswith(">") for line in block.split("\n")):
        return "quote"

    # Check for unordered list (every line starts with the same * or - followed by a space)
    lines = block.split("\n")
    if all(line.strip().startswith("* ") for line in lines) or all(line.strip().startswith("- ") for line in lines):
        return "unordered_list"

    # Check for ordered list (every line starts with a sequential number followed by '. ')
    if all(
        line.strip().split(". ")[0].isdigit()
        and ". " in line
        and int(line.strip().split(". ")[0]) == i + 1
        for i, line in enumerate(lines)
    ):
        return "ordered_list"

    # Default to normal paragraph
    return "paragraph"
