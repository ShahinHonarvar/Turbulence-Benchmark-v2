def insert_after_index(lst):
    index_for_insertion = 48
    new_element = [86, 77]
    lst.insert(index_for_insertion + 1, *new_element)
    return lst