def insert_after_index(lst):
    if 70 in lst:
        index_of_70 = lst.index(70)
        lst.insert(index_of_70 + 1, 76)
    return lst