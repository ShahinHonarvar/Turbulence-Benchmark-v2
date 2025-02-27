def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 990:
            return lst[:i + 1] + [905, 742] + lst[i + 1:]
    return lst + [905, 742]