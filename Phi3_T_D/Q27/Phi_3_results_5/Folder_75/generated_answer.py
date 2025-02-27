def insert_after_index(lst):
    index_99 = next((i for i, val in enumerate(lst) if val == 99), -1)
    return lst[:index_99 + 1] + [99] + lst[index_99 + 1:] if index_99 != -1 else lst