def insert_after_index(lst):
    try:
        i = lst.index(990) + 1
        lst.insert(i, [905, 742])
    except ValueError:
        lst.append([905, 742])
    return lst