import os
import sys
import shutil
from textnode import TextType, TextNode
from page_generator import generate_page

def clear_destination(path):
    if os.path.exists(path) == False:
        raise Exception("invalid path")
    if os.path.isfile(path): os.remove(path)
    else:
        for entry in os.listdir(path):
            entry_path = os.path.join(path, entry)
            if entry is os.path.isfile: #if file - remove file
                os.remove(entry_path)
                print(f"Removed file: {entry_path}")
            else:                       #if directory - call function again
                clear_destination(entry_path)

        try:
            os.rmdir(path)
            print(f"removed empty directory: {path}")
        except OSError:
            pass


def copy_static(path_from, path_to):

    if os.path.exists(path_from) == False:
        raise Exception("invalid path")
    
    if os.path.isfile(path_from):
        print(f"Copying file: {path_from} to {path_to}")
        os.makedirs(os.path.dirname(path_to), exist_ok=True)
        shutil.copy(path_from, path_to)

    elif os.path.isdir(path_from):
        os.makedirs(path_to, exist_ok=True)
        for entry in os.listdir(path_from):
            entry_path_from = os.path.join(path_from, entry)
            entry_path_to = os.path.join(path_to, entry)
                
            copy_static(entry_path_from, entry_path_to)


def generate_page_recursive(source_dir, destination_dir, basepath):
    template_path = os.path.expanduser("~/sitegenerator/template.html")

    for entry in os.listdir(source_dir):
        source_path = os.path.join(source_dir, entry)
        
        if os.path.isfile(source_path) and source_path.endswith(".md"):
            # Create the corresponding path in the destination directory
            destination_path = os.path.join(destination_dir, "index.html")
            
            generate_page(source_path, template_path, destination_path, basepath)


        elif os.path.isdir(source_path):  # Recurse into subdirectories
            generate_page_recursive(source_path, os.path.join(destination_dir, entry), basepath)


    
def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    source_path = os.path.expanduser("~/sitegenerator/static")
    destination_path = os.path.expanduser("~/sitegenerator/docs")

#   clear_destination(destination_path)
    copy_static(source_path, destination_path)

    content_index_path = os.path.expanduser("~/sitegenerator/content")
    destination_index_path = os.path.expanduser("~/sitegenerator/docs")
    generate_page_recursive(content_index_path, destination_index_path, basepath)

if __name__ == "__main__":
    main()