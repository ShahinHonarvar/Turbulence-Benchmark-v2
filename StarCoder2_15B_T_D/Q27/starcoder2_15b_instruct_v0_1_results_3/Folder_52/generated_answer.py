def insert_after_index(lst):
    index = 97
    value = 72.27
    new_list = lst[:]
    new_list.insert(index + 1, value)
    return new_list