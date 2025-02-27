def insert_after_index(lst):
    index_to_insert = lst.index(323) + 1
    lst[index_to_insert:index_to_insert] = [389, 303]
    return lst