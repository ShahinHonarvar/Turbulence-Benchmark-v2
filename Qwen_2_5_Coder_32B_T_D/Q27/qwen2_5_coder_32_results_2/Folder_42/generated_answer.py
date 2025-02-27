def insert_after_index(lst):
    if 44 in lst:
        index = lst.index(44) + 1
        lst.insert(index, 40)
        lst.insert(index + 1, 27)
    return lst