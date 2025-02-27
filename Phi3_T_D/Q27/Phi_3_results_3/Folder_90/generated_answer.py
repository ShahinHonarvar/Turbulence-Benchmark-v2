def insert_after_index(lst):
    if all((isinstance(item, int) for item in lst)):
        lst.insert(762, 925)
    return lst