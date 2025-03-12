from enum import Enum

class BlockType(Enum):
	PARAGRAPH = "paragraph"
	HEADING = "heading" 
	CODE = "code" 
	QUOTE = "quote" 
	UNORDERED_LIST = "unordered_list" 
	ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
	split_block = block.split("\n")
	first_line = split_block[0] if split_block else ""

	is_quote = all(block.startswith(">") for block in split_block)
	if is_quote: return BlockType.QUOTE

	if all(item.startswith(">") for item in split_block):
		return BlockType.QUOTE
	
	if block.startswith("```") and block.endswith("```"): 
		is_code = block.startswith("```") and block.endswith("```") 
		if is_code:
			return BlockType.CODE

	# Check for headings
	heading_level = 0
	if first_line.startswith("#") and len(split_block) == 1:
		for char in first_line:
			if char == '#':
				heading_level += 1
			else:
				break
    
	if (1 <= heading_level <= 6 and len(first_line) > heading_level and first_line[heading_level] == " "):
		return BlockType.HEADING
		
	if all(item.startswith(("- ", "* ")) for item in split_block):
		return BlockType.UNORDERED_LIST
	
	if len(split_block) > 0:
		is_ordered_list = True
		for i, item in enumerate(split_block, 1):
			expected_prefix = str(i) + ". "
			if not item.startswith(expected_prefix):
				is_ordered_list = False
				break
		if is_ordered_list: return BlockType.ORDERED_LIST

	return BlockType.PARAGRAPH