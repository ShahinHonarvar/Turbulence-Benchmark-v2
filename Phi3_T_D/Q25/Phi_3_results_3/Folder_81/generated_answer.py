def insert_at_index(lst):
    if len(lst) < 28:
        return None
    lst_copy = lst.copy()
    lst_copy.insert(28, 20)
    return lst_copy