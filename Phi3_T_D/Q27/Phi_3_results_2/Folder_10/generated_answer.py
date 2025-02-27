def insert_after_index(lst):
    for i, x in enumerate(lst):
        if i == 56:
            lst.insert(i + 1, 54)
            break
    return lst