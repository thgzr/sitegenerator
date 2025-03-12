from enum import Enum

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result_list = []

    for node in old_nodes:  # Loop through the list of old nodes
        if node.text_type != TextType.TEXT:
            result_list.append(node)  # Append non-text nodes as-is
            continue

        split_list = node.text.split(delimiter)  # Split the node content by the delimiter
        if len(split_list) % 2 == 0:
            raise Exception("Invalid markdown syntax: unmatched delimiters")

        for i in range(len(split_list)):
            text_type_to_use = TextType.TEXT if i % 2 == 0 else text_type
            if split_list[i]:  # Ignore empty strings (e.g., extra delimiters around text)
                result_list.append(TextNode(split_list[i], text_type_to_use))

    return result_list

