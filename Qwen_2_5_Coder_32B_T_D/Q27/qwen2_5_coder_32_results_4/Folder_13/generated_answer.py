def insert_after_index(lst):
    try:
        index = lst.index(693) + 1
    except ValueError:
        return lst
    return lst[:index] + [606, 873] + lst[index:]