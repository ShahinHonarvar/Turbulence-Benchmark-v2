def insert_after_index(list_arg):
    """
    This function takes a list as an argument and returns a new list with
    [26, 10] inserted after index 55.
    """
    new_list = list_arg[:]
    new_list.insert(56, [26, 10])
    return new_list