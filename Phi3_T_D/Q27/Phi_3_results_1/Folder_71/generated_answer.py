def insert_after_index(lst):
    try:
        position = lst.index(70)
        lst.insert(position + 1, 76)
        return lst
    except ValueError:
        return lst