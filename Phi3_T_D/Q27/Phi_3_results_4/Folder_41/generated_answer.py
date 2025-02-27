def insert_after_index(lst):
    new_elem = [78, 16]
    insert_index = 87
    return lst[:insert_index + 1] + new_elem + lst[insert_index + 1:]