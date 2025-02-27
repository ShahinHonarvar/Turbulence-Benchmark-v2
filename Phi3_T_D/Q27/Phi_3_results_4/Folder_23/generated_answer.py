def insert_after_index(lst):
    if len(lst) < 39:
        raise IndexError('List must have at least 39 elements')
    return lst[:39] + [45] + lst[39:]