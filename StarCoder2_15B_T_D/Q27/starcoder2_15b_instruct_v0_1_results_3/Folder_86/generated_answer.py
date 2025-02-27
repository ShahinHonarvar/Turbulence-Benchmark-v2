def insert_after_index(lst):
    index = 990
    new_elements = [905, 742]
    lst.insert(index + 1, *new_elements)
    return lst