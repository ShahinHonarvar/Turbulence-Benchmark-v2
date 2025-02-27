def insert_after_index(lst):
    index_to_insert = 38
    value_to_insert = 45
    if index_to_insert < len(lst):
        lst.insert(index_to_insert + 1, value_to_insert)
    return lst