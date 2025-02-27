def insert_after_index(lst):
    if 91 in lst:
        index = lst.index(91) + 1
        return lst[:index] + [46, 13] + lst[index:]
    else:
        return lst + [46, 13]