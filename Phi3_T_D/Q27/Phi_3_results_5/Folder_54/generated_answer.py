def insert_after_index(lst):
    index_to_insert = 43
    if index_to_insert < len(lst):
        lst.insert(index_to_insert + 1, 37)
    return lst