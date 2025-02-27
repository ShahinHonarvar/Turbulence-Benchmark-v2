def identical_elements(list1, list2):
    return {elem for elem in list1[1:9] if elem in list2[1:9]}