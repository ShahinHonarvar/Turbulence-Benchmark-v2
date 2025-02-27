def identical_elements(list1, list2):
    return {list1[i] for i in range(4, 9) if list1[i] in list2[4:9]}