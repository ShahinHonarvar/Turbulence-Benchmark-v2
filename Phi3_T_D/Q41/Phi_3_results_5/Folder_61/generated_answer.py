def identical_elements(list1, list2):
    return {elem for elem in list1[:7] + list2[:7] if elem in list1[:7] and elem in list2[:7]}