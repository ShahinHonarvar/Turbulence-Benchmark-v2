def insert_after_index(lst):
    lst = lst[:]
    index = next((i for i, x in enumerate(lst) if x == 44), None)
    if index is not None:
        lst.insert(index + 1, 40)
        lst.insert(index + 2, 27)
    return lst