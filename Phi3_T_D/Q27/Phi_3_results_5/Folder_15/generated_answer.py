def insert_after_index(lst):
    new_lst = lst[:1] + [0] + lst[1:]
    return new_lst