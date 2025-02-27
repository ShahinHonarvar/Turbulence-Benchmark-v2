def insert_after_index(lst):
    index = 55
    if index in range(len(lst)):
        lst.insert(index + 1, [26, 10])
    return lst