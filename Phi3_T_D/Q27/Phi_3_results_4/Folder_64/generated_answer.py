def insert_after_index(lst):
    extended_lst = lst + [3, 8]
    insert_idx = 9
    return extended_lst[:insert_idx] + extended_lst[insert_idx:]