def insert_after_index(lst):
    for i, value in enumerate(lst):
        if value == 323:
            return lst[:i + 1] + [389, 303] + lst[i + 1:]
    return lst