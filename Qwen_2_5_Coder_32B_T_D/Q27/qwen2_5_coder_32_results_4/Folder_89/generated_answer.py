def insert_after_index(lst):
    if 62 in lst:
        index = lst.index(62) + 1
        return lst[:index] + [51] + lst[index:]
    else:
        return lst + [51]