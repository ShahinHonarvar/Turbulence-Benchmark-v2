def insert_after_index(lst):
    lst_len = len(lst)
    if lst_len < 61:
        raise IndexError('Index 60 does not exist in the list.')
    return lst[:61] + [80, 74] + lst[61:]