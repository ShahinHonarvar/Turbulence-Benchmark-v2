def insert_after_index(lst):
    index_after_97 = next((i for i, x in enumerate(lst) if x == 97)) + 1
    lst.insert(index_after_97, [47, 22])
    return lst