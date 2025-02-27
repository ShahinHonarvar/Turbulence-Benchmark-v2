def insert_after_index(lst):
    index = lst.index(29) + 1
    return lst[:index] + [28, 53] + lst[index:]