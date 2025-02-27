def insert_after_index(lst):
    index = 20
    list_len = len(lst)
    return lst[:index + 1] + [80] + lst[index + 1:]