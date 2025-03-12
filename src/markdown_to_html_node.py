from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType

from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, TextType

from text_to_textnodes import text_to_textnodes
from text_to_html_node import text_node_to_html_node

def text_to_children(text):

    text_nodes = text_to_textnodes(text)

    html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    return html_nodes

def paragraph_to_html_node(block):
    block = block.replace("\n", " ")
    children = text_to_children(block)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == '#':
            level += 1
        else:
            break

    content = block[level:].strip()
    children = text_to_children(content)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)
'''
def quote_to_html_node(block):
    lines = block.split("\n")
    paragraphs = []
    current_paragraph = []
    
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        
        content = line.lstrip(">").strip()
        
        if content == "" and current_paragraph:  # Empty line indicates paragraph break
            paragraphs.append(" ".join(current_paragraph))
            current_paragraph = []
        elif content != "":  # Skip empty lines at beginning
            current_paragraph.append(content)
    
    if current_paragraph:  # Don't forget the last paragraph
        paragraphs.append(" ".join(current_paragraph))
    
    # Now create paragraph nodes for each paragraph
    children = []
    for paragraph in paragraphs:
        p_children = text_to_children(paragraph)
        children.append(ParentNode("p", p_children))
    
    return ParentNode("blockquote", children)'
'''

def unordered_list_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def ordered_list_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_blocks = []

    for block in blocks:
        block_type = block_to_block_type(block)
        print(f"DEBUG: block_type is {block_type} ({type(block_type)}) for block: {block}")

        if  block_type == BlockType.CODE:
            node = code_to_html_node(block)
        
        elif block_type == BlockType.PARAGRAPH:
            node = paragraph_to_html_node(block)

        elif block_type == BlockType.HEADING:
            node = heading_to_html_node(block)

        elif block_type == BlockType.QUOTE:
            node = quote_to_html_node(block)

        elif block_type == BlockType.UNORDERED_LIST:
            node = unordered_list_to_html_node(block)
        
        elif block_type == BlockType.ORDERED_LIST:
            node = ordered_list_to_html_node(block)

        else:
            node = paragraph_to_html_node(block)

        html_blocks.append(node)

    parent = ParentNode("div", html_blocks)
    return parent