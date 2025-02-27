def insert_at_index(lst):
    if len(lst) <= 35:
        lst.append(88)
        new_list = lst
    else:
        lst.insert(35, 88)
        new_list = lst
    return new_list