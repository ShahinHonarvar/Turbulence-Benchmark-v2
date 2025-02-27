def insert_after_index(lst):
    if len(lst) < 5:
        return lst + [7]
    lst[5:5] = [7]
    return lst