import delimeter
from markdown import extract_markdown_images, extract_markdown_links

from textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    result_list = []

    for node in old_nodes:  # Loop through the list of old nodes
        if extract_markdown_images(node.text) == []: # no images found
            result_list.append(node)  # Append non-text nodes as-is
            continue
        
        image_list = extract_markdown_images(node.text)
        current_text = node.text

        for alt_text, url in image_list:
            split_list = current_text.split(f"![{alt_text}]({url})", 1)
            if split_list[0] != "":
                result_list.append(TextNode(split_list[0], TextType.TEXT))
            result_list.append(TextNode(alt_text, TextType.IMAGE, url))
            current_text = split_list[1]
        
        if current_text != "":
            result_list.append(TextNode(current_text, TextType.TEXT))

    return result_list

def split_nodes_link(old_nodes):
    result_list = []

    for node in old_nodes:  # Loop through the list of old nodes
        if extract_markdown_links(node.text) == []: # no links found
            result_list.append(node)  # Append non-text nodes as-is
            continue

        links_list = extract_markdown_links(node.text)
        current_text = node.text

        for alt_text, url in links_list:
            split_list = current_text.split(f"[{alt_text}]({url})", 1)
            if split_list[0] != "":
                result_list.append(TextNode(split_list[0], TextType.TEXT))
            result_list.append(TextNode(alt_text, TextType.LINK, url))
            current_text = split_list[1]
        
        if current_text != "":
            result_list.append(TextNode(current_text, TextType.TEXT))

    return result_list