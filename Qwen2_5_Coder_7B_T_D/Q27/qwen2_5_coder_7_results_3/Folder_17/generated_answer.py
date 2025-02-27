def insert_after_index(lst):
    index_of_94 = lst.index(94)
    new_lst = lst[:]
    new_lst.insert(index_of_94 + 1, 93)
    return new_lst