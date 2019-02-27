import os
import argparse


def delete_spaces(root_path):

    print("Removing spaces from folders and files")

    folders_paths = []
    files_paths = []

    # Getting all paths to folders and files
    for root, folders, files in os.walk(root_path):
        
        for folder in folders:
            folder_path = os.path.join(root, folder)
            folders_paths.append(folder_path)

        for file in files:
            file_path = os.path.join(root, file)
            files_paths.append(file_path)

    # Renaming files before folders beacuse paths are relative to folders
    for file_old in files_paths:
        dirname = os.path.dirname(file_old)
        filename = os.path.basename(file_old).replace(" ", "")
        file_new = os.path.join(dirname, filename)
        os.replace(file_old, file_new)

    # Renaming folders in reverse older (bottom levels first)
    for folder_old in folders_paths[::-1]:
        dirroot = os.path.dirname(folder_old)
        dirname = os.path.basename(folder_old).replace(" ", "")
        folder_new = os.path.join(dirroot, dirname)
        os.replace(folder_old, folder_new)


if __name__ == "__main__":

    description = "Delete blank spaces from names in path recursively."
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("path",
                        help="folder path to remove the blank spaces from")
    args = parser.parse_args()

    # Getting path from args
    delete_spaces(args.path)