def insert_after_index(lst):
    index = lst.index(66)
    return lst[:index + 1] + [45] + lst[index + 1:]