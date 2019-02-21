import json


def get_dict_paths_verbose(dictionary, path="", path_list=[]):
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
        
        # path = path + "/" +  key
        path_list.append(key) 
        # print(path_list)
        print("path:---------------> " + "/".join(path_list))
        # print(path)

        # If value is a dict
        if isinstance(value, dict):
            print("down: append")
            get_dict_paths(value, path=path, path_list=path_list)    
            try:
                path_list.pop()
            except Exception as e:
                pass
            print("up  : pop")
            
        # if value print it 
        else:
            try:
                path_list.pop()
            except Exception as e:
                pass
            # # path_list.append(value)
            # print("/".join(path_list))
            pass
    
    return path


def get_dict_paths(dictionary, ret_list=[], current_path=[]):
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
        
        # Keeping track of current path in tree
        current_path.append(key) 

        # If value is a dict we iterate again
        if isinstance(value, dict):
            # Go down one level
            get_dict_paths(value, ret_list=ret_list, current_path=current_path)
            
            # Go up and popping element from current path
            current_path.pop()
            
        # If value is not a dict, just a value
        # TODO: handle lists
        else:
            # Reached final element
            # Getting unix like path
            # TODO: uncomment
            # path = "/".join(current_path) + "/" + value
            
            # not adding key of the value
            path = "/".join(current_path[:-1]) + "/" + value

            # Appending path to output list
            ret_list.append(path)

            # Printing
            print(path)

            # Popping element from path
            current_path.pop()
    
    return ret_list


def read_json(path_to_file):
    with open(path_to_file) as f:
        data = json.load(f)
    
    return data


conf = read_json("dir.json")
paths = get_dict_paths(conf, ret_list=[], current_path=[])

print("Path lists")
print(paths)