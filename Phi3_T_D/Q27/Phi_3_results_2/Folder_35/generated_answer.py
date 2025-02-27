def insert_after_index(lst):
    if len(lst) <= 100:
        return lst
    return lst[:101] + [876, 203] + lst[101:]