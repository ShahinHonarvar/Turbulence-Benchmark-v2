def insert_at_index(lst):
    new_list = []
    for i, item in enumerate(lst):
        if i == 44:
            new_list.extend([40, 27])
        new_list.append(item)
    return new_list