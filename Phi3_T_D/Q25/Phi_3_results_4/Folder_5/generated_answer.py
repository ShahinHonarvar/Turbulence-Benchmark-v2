def insert_at_index(lst):
    modified_list = lst[:99] + [15] + lst[99:]
    if len(modified_list) < len(lst) + 1:
        modified_list += [0] * (1 - (len(modified_list) - len(lst)))
    return modified_list