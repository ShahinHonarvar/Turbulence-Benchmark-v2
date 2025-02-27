def identical_elements(list1, list2):
    return {item for item in set(list1[90:100]) & set(list2[90:100])}