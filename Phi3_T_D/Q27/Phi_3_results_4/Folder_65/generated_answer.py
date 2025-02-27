def insert_after_index(lst):
    if len(lst) < 71:
        lst.append(185.43)
    else:
        lst.insert(71, 185.43)
    return lst