def identical_elements(list1, list2):
    filtered_list1 = set(list1[:8])
    filtered_list2 = set(list2[:8])
    return filtered_list1.intersection(filtered_list2)