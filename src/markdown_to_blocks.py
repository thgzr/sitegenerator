import re

def markdown_to_blocks(markdown):
    split_string = markdown.split('\n\n')
    result = []
    for item in split_string:
        if item != "": 
            clean_string = item.strip()
            result.append(clean_string)
    return result
