def identical_elements(list1, list2):
    return {list1[i] for i in range(6, 9) if list1[i] in list2[6:9]}