def identical_elements(list1, list2):
    start_index, end_index = (30, 48)
    return {list1[i] for i in range(start_index, end_index + 1) if i < len(list1) and list1[i] in list2[i]}