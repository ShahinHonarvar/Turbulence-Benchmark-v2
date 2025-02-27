def insert_after_index(lst):
    new_list = lst[:]
    index = new_list.index(87)
    new_list.insert(index + 1, 78)
    new_list.insert(index + 2, 16)
    return new_list