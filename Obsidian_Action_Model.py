import json
import glob
import csv
from pathlib import Path

DAILY_NOTES_FOLDER = r''        # This variable ultimately needs to be imported from manifest.json

def check_boxes(md_file):
    with open(md_file, 'r') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        if '- [ ]' in line:
            lines[i] = line.replace('- [ ]', '- [x]')
            
    with open(md_file, 'w') as f:
        f.writelines(lines)

def read_tasks_from_file(md_file):
    """Read through individual Markdown file and output list of tagged tasks."""
    
    tasks_in_file = []      # Initialize list to be stored in csv

    try:
        with open(md_file, 'r') as f:   # Read lines from the file
            lines = f.readlines()

        for i, line in enumerate(lines):
            if '- [ ]' in line:
                tags, text = parse_task_info(lines[i])
                is_completed = False
                tasks_in_file.append([tags, text, is_completed])

    except:
        print(f'Unable to read tasks at: {md_file}')

    return list(tasks_in_file)

def gather_tasks_from_directory(tasks_directory, save_directory):
    """Scans all Markdown files in a directory and saves tasks from them to a csv file."""

    # TODO: Add in bit that skips a file if it's already been scanned in pdf format

    file_list = glob.glob(tasks_directory)

    all_tasks = []

    for file in file_list:
        file_tasks = read_tasks_from_file(file)
        
        for task in file_tasks:
            all_tasks.append(task)
    
    save_file = Path(save_directory) / 'tasks_backup.csv'

    with open(save_file, 'w', newline='') as file:
        writer = csv.writer(file)

        for task in all_tasks:
            writer.writerow([task])
    
    print('Saved to csv file.')

def parse_task_info(task):
    """Reads the text content of each task and separates them out."""
    tags = '#test'    # Parse out the tag(s) the task was tagged with #like_list 
                
                 # TODO: If a task lacks a tag, make sure to tag it as '#untagged'

    text = f'{task}'    # Parse out the text following the tag that is then passed to the next script
    
    return tags, text

def specify_directory(directory_path = DAILY_NOTES_FOLDER):
    # TODO: Add code here that looks at every Markdown file in the directory 
    # By default, the directory should be the Daily Notes folder
    pass

def read_settings(json_file):
    """Reads user settings from 'manifest.json'"""
    save_directory = ''         # Read from JSON file
    tasks_directory = ''        # Read from JSON file
    assigned_tags = [[],[]]     # Read from JSON file

    return save_directory, tasks_directory, assigned_tags
    
def __main__():
    pass

# print(read_tasks_from_file('README.md'))


# gather_tasks_from_directory(tasks_directory, save_directory)