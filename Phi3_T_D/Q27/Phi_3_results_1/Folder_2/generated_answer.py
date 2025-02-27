def insert_after_index(lst):
    index_to_insert_after = 427
    elements_to_insert = [312, 441]
    lst.insert(index_to_insert_after + 1, *elements_to_insert)
    return lst