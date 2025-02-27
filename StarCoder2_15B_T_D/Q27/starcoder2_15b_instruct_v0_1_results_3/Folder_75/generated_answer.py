def insert_after_index(lst):
    return lst[:lst.index(99) + 1] + [99] + lst[lst.index(99) + 1:]