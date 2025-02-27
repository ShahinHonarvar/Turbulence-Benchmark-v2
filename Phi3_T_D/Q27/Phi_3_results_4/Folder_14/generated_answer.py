def insert_after_index(lst):
    if len(lst) <= 16:
        return lst + [550.97]
    else:
        lst.insert(16, 550.97)
        return lst