def insert_after_index(lst):
    index = lst.index(99) if 99 in lst else -1
    if index != -1:
        lst.insert(index + 1, 99)
    return lst