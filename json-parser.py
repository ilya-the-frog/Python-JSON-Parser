import os
import json

def print_tree(data, level=0):
    """
    Prints the nested JSON data as a tree structure
    """
    for key, value in data.items():
        print(f"{'  ' * level}- {key}")
        if isinstance(value, dict):
            print_tree(value, level+1)
        else:
            print(f"{'  ' * (level+1)}- {value}")

# Set current directory to search for JSON files
directory = os.getcwd()

# Search for JSON files in the directory
json_files = [f for f in os.listdir(directory) if f.endswith('.json')]

if not json_files:
    print("No JSON files found in the directory.")
else:
    print("Found the following JSON files in the directory:")
    for i, f in enumerate(json_files):
        print(f"{i+1}. {f}")

    # Ask the user to select a file to open
    while True:
        selection = input("Enter the number of the JSON file you want to open: ")
        try:
            selection = int(selection)
            if 1 <= selection <= len(json_files):
                break
            else:
                print(f"Selection must be a number between 1 and {len(json_files)}")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Open the selected file
    selected_file = os.path.join(directory, json_files[selection-1])
    with open(selected_file, 'r') as f:
        data = json.load(f)

    # Loop to get the user input and return the corresponding values
    while True:
        key = input("Enter a JSON key (or 'quit' to exit): ")
        if key == 'quit':
            break
        value = data
        try:
            for k in key.split('.'):
                value = value[k]
            if isinstance(value, dict):
                print_tree(value)
            else:
                print(value)
        except KeyError:
            print("Invalid key. Please enter a valid key.")
