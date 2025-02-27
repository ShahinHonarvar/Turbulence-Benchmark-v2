def insert_after_index(lst):
    new_lst = lst.copy()
    index = 96 - len(lst) + 1
    new_lst.insert(index, 36)
    return new_lst