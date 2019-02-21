def get_dict_paths(dictionary, path="", path_list=[]):
    """Loops over a dictionary tree
    
    Parameters
    ----------
    dictionary : dict
        dict to iterate over

    Returns
    -------
    paths_list : list
        List with dict path for each element in dict
    
    """

    for (key, value) in dictionary.items():
        
        path = path + "/" + key
        # path = path_conc(path, key)

        # print("%s" % path, end="")

        # If value is a dict
        if isinstance(value, dict):
            get_dict_paths(value, path=path, path_list=path_list)

        # If value is a value
        elif isinstance(value, list):
            for element in value:
                get_dict_paths(element, path=path, path_list=path_list)
        else:
            print(path+value)
            path_list.append(path+value)
    
    return path_list
