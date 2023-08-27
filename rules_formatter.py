
import argparse
import os

def format_rules_file_content(file_content):
    formatted_content = []
    formatted_content.append(file_content[0])
    formatted_content.append("payload:\n")
    for line in file_content[1:]:
        if "/" in line:
            formatted_content.append("  - " + line)
        else:
            formatted_content.append(line)
    return "".join(formatted_content)

def format_single_file(file_path):
    with open(file_path, 'r') as f:
        content = f.readlines()
    formatted_content = format_rules_file_content(content)
    with open(file_path, 'w') as f:
        f.write(formatted_content)

def format_directory(directory_path):
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".rules"):
            file_path = os.path.join(directory_path, file_name)
            format_single_file(file_path)

def main():
    parser = argparse.ArgumentParser(description='Format .rules files.')
    parser.add_argument('--file', type=str, help='Path to the .rules file to format.')
    parser.add_argument('--folder', type=str, help='Path to the directory containing .rules files to format.')
    parser.add_argument('path', type=str, nargs='?', help='Path to the file or directory. If this is the only argument, the program will auto-detect whether it is a file or directory.')

    args = parser.parse_args()

    if args.file:
        format_single_file(args.file)
    elif args.folder:
        format_directory(args.folder)
    elif args.path:
        if os.path.isfile(args.path):
            format_single_file(args.path)
        elif os.path.isdir(args.path):
            format_directory(args.path)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
