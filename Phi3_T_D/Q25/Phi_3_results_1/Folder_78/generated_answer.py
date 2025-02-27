def insert_at_index(lst):
    lst_length = len(lst)
    if lst_length >= 63:
        lst.insert(63, 99)
        return lst
    else:
        return lst + [99] * (63 - lst_length + 1)