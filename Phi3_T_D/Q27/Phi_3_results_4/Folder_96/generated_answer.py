def insert_after_index(lst):
    index = 74
    new_value = [51, 29]
    lst.insert(index + 1, *new_value)
    return lst