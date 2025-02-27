def insert_at_index(lst):
    if len(lst) <= 696:
        lst.append(477)
    else:
        lst.insert(696, 477)
    return lst