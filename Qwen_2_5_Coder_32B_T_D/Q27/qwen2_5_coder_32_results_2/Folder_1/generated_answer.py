def insert_after_index(lst):
    if len(lst) > 93:
        lst = lst[:94] + [33, 78] + lst[94:]
    else:
        lst = lst + [33, 78]
    return lst