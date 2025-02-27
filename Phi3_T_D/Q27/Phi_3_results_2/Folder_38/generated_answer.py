def insert_after_index(lst):
    target_index = 89
    value_to_insert = 86
    if target_index < len(lst):
        lst.insert(target_index + 1, value_to_insert)
    return lst