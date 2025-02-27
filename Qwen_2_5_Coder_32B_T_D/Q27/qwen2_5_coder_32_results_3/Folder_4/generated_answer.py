def insert_after_index(lst):
    if 60 in lst:
        index = lst.index(60)
        lst = lst[:index + 1] + [80, 74] + lst[index + 1:]
    return lst