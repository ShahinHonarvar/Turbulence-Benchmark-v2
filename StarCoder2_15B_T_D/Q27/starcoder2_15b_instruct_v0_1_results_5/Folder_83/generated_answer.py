def insert_after_index(lst):
    modified_list = []
    for i, element in enumerate(lst):
        if i == 13:
            modified_list.extend([56, 54])
        modified_list.append(element)
    return modified_list