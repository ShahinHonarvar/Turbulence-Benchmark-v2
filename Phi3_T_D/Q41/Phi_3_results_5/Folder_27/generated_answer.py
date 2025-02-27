def identical_elements(list1, list2):
    return {elem for idx, elem in enumerate(list1[66:94]) if elem in list2[66:94]}