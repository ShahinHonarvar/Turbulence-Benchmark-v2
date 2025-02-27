def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 427:
            return lst[:i + 1] + [312, 441] + lst[i + 1:]
    return lst