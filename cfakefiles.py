"""Copy N files from 'path_from' to 'path_to'
"""


import sys
import os
from shutil import copyfile

import argparse


def path_conc(abs_path, new_path):
    """Concatenate path making sure there is no problem with '/'    
    """
    abs_end = abs_path[-1]
    path_init = new_path[0]

    if abs_end is not "/" and path_init is not "/":
        # No one had / so we add it
        conc_path = abs_path + "/" + new_path

    elif abs_end is "/" and path_init is "/":
        # Both had / so removing one
        conc_path = abs_path + new_path[1:]

    else:
        # Only one had / so safe to concatenate
        conc_path = abs_path + new_path

    return conc_path

# Parsing args
parser = argparse.ArgumentParser()
parser.add_argument("N", help="Number of fake files to create")
parser.add_argument("extension", help="extension of the files to create")
parser.add_argument("path_to", help="Path where to create the files")

args = parser.parse_args()

N = int(args.N)
extension = args.extension
path_to = args.path_to

# Making sure extension starts with '.'
if extension[0] != ".":
    extension = "." + extension

for i in range(N):
    filename = "file" + str(i) + extension
    file = path_conc(path_to, filename)
    print("Creating " + file)
    f = open(file, "w+")
    f.close()