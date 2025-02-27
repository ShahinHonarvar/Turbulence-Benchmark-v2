def insert_after_index(lst):
    index_85 = [i for i, x in enumerate(lst) if x == 85][0]
    lst.insert(index_85 + 1, [41, 95])
    return lst