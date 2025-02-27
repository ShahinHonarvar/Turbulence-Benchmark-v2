def insert_after_index(lst):
    if 56 in lst:
        index = lst.index(56)
        lst = lst[:index + 1] + [54] + lst[index + 1:]
    return lst