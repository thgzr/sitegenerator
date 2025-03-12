def extract_title(markdown):
    split_lines = markdown.split("\n")
    extracted_title = ""
    for line in split_lines:
        stripped_line = line.strip()
        if stripped_line[0] == "#" and stripped_line[1] != "#": #title is found
            extracted_title = stripped_line
            break
    
    if extracted_title == "": #no title is found
        raise Exception("no title is found")
    
    if extracted_title[1] == " ":
        return extracted_title[2:]
    else: 
        return extracted_title[1:]