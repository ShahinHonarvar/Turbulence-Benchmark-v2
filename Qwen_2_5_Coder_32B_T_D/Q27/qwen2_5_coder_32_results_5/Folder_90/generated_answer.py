def insert_after_index(lst):
    index = lst.index(761) + 1
    return lst[:index] + [925] + lst[index:]