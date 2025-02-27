def insert_after_index(lst):
    index = next((i for i, value in enumerate(lst) if value == 89), None)
    if index is not None:
        lst.insert(index + 1, 86)
    return lst