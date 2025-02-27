def insert_at_index(lst):
    if len(lst) > 500:
        lst.insert(500, [912, 170])
    else:
        lst.extend([None] * (500 - len(lst)) + [[912, 170]])
    return lst