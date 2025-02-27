def insert_after_index(lst):
    index = 8
    if len(lst) < index + 1:
        return lst + [3, 8]
    lst.insert(index + 1, 3, 8)
    return lst