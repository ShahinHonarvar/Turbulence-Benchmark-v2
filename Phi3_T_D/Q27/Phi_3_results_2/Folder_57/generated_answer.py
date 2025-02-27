def insert_after_index(lst):
    index = lst.index(80) if 80 in lst else None
    if index is not None and index < 90:
        lst.insert(index + 2, 80)
    elif index is not None:
        lst.insert(91, 80)
    else:
        lst.insert(91, 80)
    return lst