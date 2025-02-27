def identical_elements(list1, list2):
    return {value for value in list1[1:6] if value in list2[1:6]}