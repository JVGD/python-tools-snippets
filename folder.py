def find_folder(path, foldername):
    """Find folders with 'name' in path
    
    Parameters
    ----------
    path : str
        Path in which do the searching
    foldername : str
        Folder name
    
    Returns
    -------
    paths_list
        List with paths to 'foldername' folder
    """

    # Supporting all wildcard
    if foldername == "*":
        # empty string will match all in .endswith("")
        foldername = ""

    # Return path list
    paths_list = []

    for path, dirs, files in os.walk(path):

        # Find recursively in directory tree
        # if finds an image or annotation folder
        # it appends it to the list of paths to return
        if path.endswith(foldername):
            paths_list.append(path)
            logger.debug("Found: %s", path)

    return paths_list
