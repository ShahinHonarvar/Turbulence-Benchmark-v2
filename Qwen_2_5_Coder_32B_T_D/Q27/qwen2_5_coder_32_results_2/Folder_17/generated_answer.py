def insert_after_index(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == 94:
            lst.insert(i + 1, 93)
            break
    return lst