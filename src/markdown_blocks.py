def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    good_blocks = []
    for block in blocks:
        if block == "":
            continue
        good_blocks.append(block.strip())

    return good_blocks