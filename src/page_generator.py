import os

from markdown_to_html_node import markdown_to_html_node
from markdown_parser import extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"generating path{from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        markdown_content = file.read()

    with open(template_path, "r") as file:
        template_content = file.read()

    html_page = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)

    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html_page)
    template_content = template_content.replace('href="/', f'href="{basepath}')
    template_content = template_content.replace('src="/', f'src="{basepath}')

    directory = os.path.dirname(dest_path)
    os.makedirs(directory, exist_ok = True)

    with open(dest_path, "w") as file:
        file.write(template_content)

    print(f"File written to: {dest_path}")
