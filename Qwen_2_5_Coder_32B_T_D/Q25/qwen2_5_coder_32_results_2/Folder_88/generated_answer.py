def insert_at_index(lst):
    if len(lst) > 90:
        lst.insert(91, [46, 13])
    else:
        lst.extend([None] * (91 - len(lst)) + [[46, 13]])
    return lst