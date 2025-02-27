def insert_after_index(lst):
    new_lst = lst[:]
    index = lst.index(696) + 1
    new_lst.insert(index, 477)
    return new_lst