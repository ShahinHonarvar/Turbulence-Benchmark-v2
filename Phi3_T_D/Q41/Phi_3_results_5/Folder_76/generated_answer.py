def identical_elements(list1, list2):
    result_set = {list1[i] for i in range(686, 988) if i < len(list1) and i < len(list2) and (list1[i] == list2[i])}
    return result_set