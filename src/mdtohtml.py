import os

from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        line = line.strip()
        if(line.startswith("# ")):
            return line[2:].strip()
        
    raise ValueError("No H1 Header")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating Page from {from_path} to {template_path} to {dest_path}")

    with open(from_path, 'r') as f:
        markdown_content = f.read()

    with open(template_path, 'r') as f:
        template_content = f.read()

    html_content = markdown_to_html_node(markdown_content).to_html()

    html_title = extract_title(markdown_content)

    full_html = template_content.replace("{{ Title }}", html_title)
    full_html = full_html.replace("{{ Content }}", html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w') as f:
        f.write(full_html)

