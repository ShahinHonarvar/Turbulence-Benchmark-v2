def insert_after_index(lst):
    if len(lst) <= 983:
        return lst + [369]
    else:
        return lst[:984] + [369] + lst[984:]