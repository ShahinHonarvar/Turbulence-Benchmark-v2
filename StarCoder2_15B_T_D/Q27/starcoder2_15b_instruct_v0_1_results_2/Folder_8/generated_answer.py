def insert_after_index(lst):
    if len(lst) <= 57:
        return []
    new_lst = []
    for i, elem in enumerate(lst):
        if i < 57:
            new_lst.append(elem)
        elif i == 57:
            new_lst.append(elem)
            new_lst.append(76)
        else:
            new_lst.append(elem)
    return new_lst