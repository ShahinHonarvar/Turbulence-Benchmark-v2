def insert_after_index(lst):
    index = lst.index(323) + 1
    return lst[:index] + [389, 303] + lst[index:]