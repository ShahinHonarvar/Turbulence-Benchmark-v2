def identical_elements(list1, list2):
    return {val for val in list1[20:31] + list2[20:31] if val in list1[20:31] and val in list2[20:31]}