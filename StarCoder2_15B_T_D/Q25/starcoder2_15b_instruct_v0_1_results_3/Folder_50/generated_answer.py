def insert_at_index(my_list):
    """
    Insert the value 38 at index 52 in the given list and return a new list.
    """
    new_list = my_list[:]
    new_list.insert(52, 38)
    return new_list