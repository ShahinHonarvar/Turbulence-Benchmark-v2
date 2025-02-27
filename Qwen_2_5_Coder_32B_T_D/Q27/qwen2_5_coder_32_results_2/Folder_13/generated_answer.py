def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 693:
            return lst[:i + 1] + [606, 873] + lst[i + 1:]
    return lst