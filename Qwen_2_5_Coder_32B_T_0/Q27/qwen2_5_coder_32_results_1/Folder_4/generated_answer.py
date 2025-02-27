def insert_after_index(lst):
    index = lst.index(60) + 1
    return lst[:index] + [80, 74] + lst[index:]