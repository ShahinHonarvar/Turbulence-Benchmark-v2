def identical_elements(list1, list2):
    return {elem for elem in set(list1[:9]) & set(list2[:9])}