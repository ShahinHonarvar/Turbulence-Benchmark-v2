def insert_at_index(lst, index=0):
    return lst[:index] + [0] + lst[index:]