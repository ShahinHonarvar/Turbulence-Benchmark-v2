def insert_at_index(lst):
    lst_len = len(lst)
    if lst_len == 63:
        lst.append(99)
    elif lst_len > 63:
        lst.insert(63, 99)
    return lst