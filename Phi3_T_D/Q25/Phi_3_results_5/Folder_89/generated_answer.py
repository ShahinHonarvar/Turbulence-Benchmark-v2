def insert_at_index(lst):
    if 62 < len(lst):
        lst.insert(62, 51)
    else:
        for i in range(len(lst), 62):
            lst.append(0)
        lst.insert(62, 51)
    return lst