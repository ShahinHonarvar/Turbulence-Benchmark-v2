def insert_after_index(lst):
    x = lst[:64]
    x.append(99)
    x.extend(lst[64:])
    return x