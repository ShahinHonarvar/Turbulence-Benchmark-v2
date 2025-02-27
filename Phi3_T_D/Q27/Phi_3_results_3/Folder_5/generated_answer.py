def insert_after_index(lst):
    if not isinstance(lst, list) or 99 not in lst:
        return lst
    index_99 = lst.index(99)
    return lst[:index_99 + 1] + [15] + lst[index_99 + 1:]