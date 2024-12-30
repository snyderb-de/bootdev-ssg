def markdown_to_blocks(markdown):
    # Split the markdown string into blocks using double newlines as a separator
    raw_blocks = markdown.split("\n\n")
    
    # Process each block to strip whitespace and filter out empty blocks
    blocks = [block.strip() for block in raw_blocks if block.strip()]
    
    return blocks
