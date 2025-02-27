def insert_after_index(lst):
    if len(lst) < 96:
        return lst
    modified_list = lst[:96]
    modified_list.append(43)
    modified_list.extend(lst[96:])
    return modified_list