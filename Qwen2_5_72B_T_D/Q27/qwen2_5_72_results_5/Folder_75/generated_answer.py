def insert_after_index(lst):
    if 99 < len(lst):
        lst.insert(99, 99)
    else:
        lst.append(99)
    return lst