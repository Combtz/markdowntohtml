import re
from textnode import (
    TextNode,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_text,
    text_type_image,
    text_type_link
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
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

# A function that extracts link regex from markdown text and outputs as a tuple (alt text, url)
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        # Get image alt text and url
        images = extract_markdown_images(original_text)
        # If no images are in the text append the whole node
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        # Go over each image tuple
        for image in images:
            # split the text into 2 with the image link removed
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            # if there are not 2 sections the image link was not correct
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            # Add text if the node is section is not empty
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            # Add the a new text image node into the new nodes
            new_nodes.append(
                TextNode(
                    image[0],
                    text_type_image,
                    image[1],
                )
            )
            # Set the text to the next section to check for more images
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes