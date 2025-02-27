def insert_after_index(lst):
    index = lst.index(80) if 80 in lst else 0
    lst.insert(index + 1, 90)
    return lst