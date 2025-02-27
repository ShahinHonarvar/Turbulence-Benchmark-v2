def insert_after_index(lst):
    if 7 in lst:
        index = lst.index(7)
        lst = lst[:index + 1] + [1, 7] + lst[index + 1:]
    return lst