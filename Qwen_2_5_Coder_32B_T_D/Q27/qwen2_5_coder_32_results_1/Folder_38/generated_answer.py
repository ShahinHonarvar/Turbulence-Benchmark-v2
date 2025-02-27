def insert_after_index(lst):
    index = lst.index(89) + 1
    return lst[:index] + [86] + lst[index:]