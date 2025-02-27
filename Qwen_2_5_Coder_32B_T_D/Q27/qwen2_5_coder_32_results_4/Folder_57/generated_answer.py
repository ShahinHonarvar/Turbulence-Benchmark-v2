def insert_after_index(lst):
    index_90 = lst.index(90)
    return lst[:index_90 + 1] + [80] + lst[index_90 + 1:]