def insert_after_index(lst):
    if 87 < len(lst):
        lst = lst[:88] + [78, 16] + lst[88:]
    else:
        lst.extend([78, 16])
    return lst