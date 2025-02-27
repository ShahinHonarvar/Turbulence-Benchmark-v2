def insert_after_index(lst):
    index_to_insert = 38
    if index_to_insert < len(lst) - 1:
        lst.insert(index_to_insert + 1, [27, 34])
    return lst