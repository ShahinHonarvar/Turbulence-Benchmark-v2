def insert_after_index(lst):
    index = 42
    if index < len(lst):
        lst.insert(index + 1, 53)
    else:
        lst.append(53)
    return lst