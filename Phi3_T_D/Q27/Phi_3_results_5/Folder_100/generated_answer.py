def insert_after_index(lst):
    index_to_insert = 73
    element_to_insert = 418.88
    if index_to_insert < len(lst):
        lst.insert(index_to_insert + 1, element_to_insert)
    return lst