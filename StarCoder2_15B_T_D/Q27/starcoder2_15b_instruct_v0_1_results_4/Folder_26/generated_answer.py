import inspect

def insert_after_index(lst):
    """
    Insert the value 26 at the index immediately succeeding index 55 in the given list.
    """
    lst.insert(55 + 1, 26)
    return lst