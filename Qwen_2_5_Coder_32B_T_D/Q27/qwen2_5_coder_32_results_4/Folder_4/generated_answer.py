def insert_after_index(lst):
    index_60 = lst.index(60)
    return lst[:index_60 + 1] + [80, 74] + lst[index_60 + 1:]