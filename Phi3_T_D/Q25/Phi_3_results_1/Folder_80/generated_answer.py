def insert_at_index(lst):
    if len(lst) < 95:
        lst = lst + [0] * (95 - len(lst))
    lst.insert(95, 43)
    return lst