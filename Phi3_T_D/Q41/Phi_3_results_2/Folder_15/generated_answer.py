def identical_elements(list1, list2):
    required_set = set(list1[2:4] + list2[2:4])
    return {item for item in required_set if item in list1[2:4] and item in list2[2:4]}