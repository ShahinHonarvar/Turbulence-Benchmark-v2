def identical_elements(list1, list2):
    return {x for x in set(list1[6:9]) & set(list2[6:9])}