def identical_elements(list1, list2):
    return {el for el in set(list1[30:200]) if el in set(list2[30:200])}