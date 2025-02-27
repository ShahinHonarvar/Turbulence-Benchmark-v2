def identical_elements(list1, list2):
    return {elem for elem in set(list1[30:48]) & set(list2[30:48])}