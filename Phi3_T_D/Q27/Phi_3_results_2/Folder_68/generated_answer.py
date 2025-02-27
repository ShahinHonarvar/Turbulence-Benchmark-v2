def insert_after_index(lst):
    new_lst = lst.copy()
    if len(new_lst) <= 7:
        new_lst.append(1, 7)
    else:
        new_lst.insert(8, 1, 7)
    return new_lst