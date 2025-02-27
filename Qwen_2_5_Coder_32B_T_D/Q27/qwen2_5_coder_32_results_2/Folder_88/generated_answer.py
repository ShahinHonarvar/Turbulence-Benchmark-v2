def insert_after_index(lst):
    if 91 in lst:
        index = lst.index(91) + 1
        lst.insert(index, 46)
        lst.insert(index + 1, 13)
    return lst