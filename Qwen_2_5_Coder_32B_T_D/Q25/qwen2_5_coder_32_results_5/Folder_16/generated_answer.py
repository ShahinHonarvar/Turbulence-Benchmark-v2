def insert_at_index(lst):
    if len(lst) >= 983:
        lst.insert(983, 369)
    else:
        lst.extend([None] * (983 - len(lst)) + [369])
    return lst