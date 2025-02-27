def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 56:
            lst.insert(i + 1, 54)
            break
    return lst