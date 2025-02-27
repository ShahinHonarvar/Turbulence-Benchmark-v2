def insert_after_index(lst):
    try:
        idx = lst.index(693) + 1
        lst[idx:idx] = [606, 873]
    except ValueError:
        lst.append([606, 873])
    return lst