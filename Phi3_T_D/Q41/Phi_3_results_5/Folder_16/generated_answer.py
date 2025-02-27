def identical_elements(list1, list2):
    return {list1[i] for i in range(33, 37) if i < len(list1) and i < len(list2) and (list1[i] == list2[i])}