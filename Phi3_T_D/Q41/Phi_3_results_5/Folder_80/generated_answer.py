def identical_elements(list1, list2):
    return {list1[i] for i in range(64, 67) if i < len(list1) and list1[i] in list2[i]}