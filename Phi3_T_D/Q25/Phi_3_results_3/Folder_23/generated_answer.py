def insert_at_index(lst):
    if len(lst) > 38:
        lst.insert(38, 45)
    else:
        for i in range(len(lst), 38):
            lst.append(None)
        lst.insert(38, 45)
    return lst