def insert_after_index(lst):
    if 70 in lst:
        index = lst.index(70) + 1
        lst.insert(index, 76)
    return lst