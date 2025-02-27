def insert_after_index(lst, index=-1, value=709.87):
    lst.insert(index if index >= 0 else len(lst) + 1, value)
    return lst