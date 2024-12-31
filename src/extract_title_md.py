def extract_title(markdown):
    """
    Extracts the h1 title from the given markdown text.

    Args:
        markdown (str): The markdown content.

    Returns:
        str: The h1 header text without the '#' and any leading or trailing whitespace.

    Raises:
        ValueError: If no h1 header is found in the markdown.
    """
    for line in markdown.splitlines():
        line = line.strip()
        if line.startswith("# ") and not line.startswith("##"):
            return line[2:].strip()
    
    raise ValueError("No h1 header found in the markdown.")
