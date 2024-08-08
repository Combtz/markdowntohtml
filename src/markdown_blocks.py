from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node
from htmlnode import ParentNode

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

# A function that converts markdown blocks into text
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    good_blocks = []
    for block in blocks:
        if block == "":
            continue
        good_blocks.append(block.strip())

    return good_blocks

# A function that outputs the type of a block.
def block_to_block_type(block):
    lines = block.split("\n")
    # Headings 1-6
    if (
        block.startswith("# ") or
        block.startswith("## ") or
        block.startswith("### ") or
        block.startswith("#### ") or
        block.startswith("##### ") or
        block.startswith("###### ")
    ):
        return block_type_heading
    # Code block
    if (len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith('```')):
        return block_type_code
    # Quote
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    # Unordered list starting with * 
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
            return block_type_ulist
    # Unordered list starting with -
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
            return block_type_ulist
    # Ordered list starting with {int++}. 
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph
        
# Converts a full markdown document to html nodes wrapped in a div element
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

# Helper function, checks block type and converts to correct html node.
def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_olist:
        return olist_to_html_node(block)
    if block_type == block_type_ulist:
        return ulist_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)

# Converts one line of text into the correct htmlnodes
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

# Coverts one paragraph into a p element with children.
def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

# Converts heading into a h<level> element with children.
def heading_to_html_node(block):
    level = 0
    # Find the level of heading
    for char in block:
        if char == "#":
            level +=1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Incorrect heading level: {level}")
    # Take the text from the block.
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    if not block.startswith('```') or not block.endswith('```'):
        raise ValueError("Invalid Code Block")
    text = block[3:-3]
    text = text.strip('\n')
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def olist_to_html_node(block):
    items = block.split('\n')
    list_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        list_items.append(ParentNode("li", children))
    return ParentNode("ol", list_items)

def ulist_to_html_node(block):
    items = block.split('\n')
    list_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        list_items.append(ParentNode("li", children))
    return ParentNode("ul", list_items)

def quote_to_html_node(block):
    lines = block.split('\n')
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid block quote")
        new_lines.append(line[2:])
    text = " ".join(new_lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)