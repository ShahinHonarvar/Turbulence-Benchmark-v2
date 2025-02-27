def insert_at_index(lst):
    if len(lst) < 412:
        lst.extend([None] * (412 - len(lst)))
    lst.insert(412, 668)
    return lst