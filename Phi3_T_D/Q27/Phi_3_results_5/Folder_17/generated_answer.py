def insert_after_index(lst):
    idx_94 = next((i for i, x in enumerate(lst) if x == 94), None)
    return lst[:idx_94 + 1] + [93] + lst[idx_94 + 1:] if idx_94 is not None else lst