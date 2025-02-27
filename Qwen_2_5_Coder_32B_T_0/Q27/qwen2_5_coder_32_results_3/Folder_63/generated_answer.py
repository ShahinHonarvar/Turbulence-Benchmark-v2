def insert_after_index(lst):
    if 76 in lst:
        index = lst.index(76) + 1
        lst = lst[:index] + [15, 51] + lst[index:]
    return lst