def identical_elements(list1, list2):
    common_elements = {list1[i] for i in range(42, 69) if i < len(list1) and i < len(list2) and (list1[i] == list2[i])}
    return common_elements