def insert_at_index(lst):
    lst_len = len(lst)
    if lst_len > 30:
        return lst[:31] + [88, 51] + lst[31:]
    else:
        return lst + [88, 51]