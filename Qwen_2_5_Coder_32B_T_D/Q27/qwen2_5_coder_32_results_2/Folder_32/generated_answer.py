def insert_after_index(lst):
    if len(lst) > 76:
        lst.insert(77, 10.01)
    else:
        lst.extend([None] * (77 - len(lst)) + [10.01])
    return lst