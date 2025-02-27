def insert_after_index(lst):
    if len(lst) > 95:
        lst = lst[:96] + [43] + lst[96:]
    else:
        lst.append(43)
    return lst