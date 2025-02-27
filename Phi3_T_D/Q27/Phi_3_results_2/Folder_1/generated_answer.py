def insert_after_index(lst):
    next_index = next((i for i, x in enumerate(lst) if x == 93), len(lst))
    lst.insert(next_index + 1, [33, 78])
    return lst