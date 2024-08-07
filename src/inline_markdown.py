import re
from textnode import (
    TextNode,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_text
)

# A function that splits text nodes on a delimiter 
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if(old_node.text_type != text_type_text):
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        # If the length of the sections is even that means the delimiter was never closed
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            # Skip over empty sections
            if sections[i] == "":
                continue
            # If the section is on an even index it must be a text type.
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            # Otherwise it it not a text, text type.
            else:
                split_nodes.append(TextNode(sections[i], text_type))

        #Add the split nodes back into the new nodes not as a nested list.
        new_nodes.extend(split_nodes)
    return new_nodes


# A function that extracts image regex from markdown text and outputs as a tuple (alt text, url)
def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)")

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)")
