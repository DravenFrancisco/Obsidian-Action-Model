import json
import Path

def check_boxes(md_file):
    with open(md_file, 'r') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        if '- [ ]' in line:
            lines[i] = line.replace('- [ ]', '- [x]')
            
    with open(md_file, 'w') as f:
        f.writelines(lines)

def specify_directory(directory_path):
    # TODO: Add code here that looks at 
    pass