def insert_after_index(lst):
    try:
        index = lst.index(80)
        if index > 90:
            lst.insert(index + 1, 80)
        return lst
    except ValueError:
        lst.insert(91, 80)
        return lst