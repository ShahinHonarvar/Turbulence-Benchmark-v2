def insert_after_index(lst):
    for i, x in enumerate(lst):
        if x == 693:
            return lst[:i + 1] + [606, 873] + lst[i + 1:]