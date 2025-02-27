def insert_at_index(lst):
    lst_length = len(lst)
    lst.insert(55, [26, 10])
    while len(lst) < lst_length + 1:
        lst.append(None)
    return lst