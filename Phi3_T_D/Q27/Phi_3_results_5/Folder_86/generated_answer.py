def insert_after_index(lst):
    index = 990
    new_list = lst[:index + 1] + [905, 742] + lst[index + 1:]
    return new_list