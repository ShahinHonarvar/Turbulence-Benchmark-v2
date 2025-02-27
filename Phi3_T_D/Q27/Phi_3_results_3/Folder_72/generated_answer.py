def insert_after_index(lst):
    index_to_insert_after = 24
    elements_to_insert = [98, 22]
    lst.insert(index_to_insert_after + 1, *elements_to_insert)
    return lst