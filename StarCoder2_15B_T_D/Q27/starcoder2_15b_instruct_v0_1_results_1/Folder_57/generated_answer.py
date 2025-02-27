def insert_after_index(lst):
    index_of_90 = lst.index(90)
    new_index = index_of_90 + 1
    lst.insert(new_index, 80)
    return lst