"""Copy N files from 'path_from' to 'path_to'
"""


import sys
import os
from shutil import copyfile

import argparse


# Parsing args
parser = argparse.ArgumentParser()
parser.add_argument("N", help="Number of files to copy")
parser.add_argument("path_from", help="Path to copy files from")
parser.add_argument("path_to", help="Path to copy files to")
args = parser.parse_args()

N = int(args.N)
path_from = args.path_from
path_to = args.path_to


# Very weird way to get files and folders in 'path_from'
for root_name, folder, files in os.walk(path_from):

    # Put files in order python does not by default
    files = sorted(files)

    # Now we have all the files in 'files'
    for i, file in enumerate(files):
        
        file_in = path_from + "/" + file
        file_out = path_to + "/" + file

        copyfile(file_in, file_out)

        # Copy only N files    
        if i == N-1:
            break
        