def insert_after_index(lst):
    index = 76
    element = [15, 51]
    new_list = lst[:]
    new_list.insert(index + 1, element)
    return new_list